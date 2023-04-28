import json
import os

import polars as pl

rootdir = "/mnt/analysisdata"
work_folder = "ifo-de-vo-ifohack2023-admin-prod-analysis-data-work"

# read eval dataset (ground truth)
df_eval = pl.read_csv(
    "IBS_paneldata_public_eval.csv",
    has_header=True,
).with_columns(pl.all().cast(pl.Int64))


df_eval = df_eval.sort(["year", "idnum", "month"])
n = 90

df_list = []
for i in range(1, n + 1):
    submission_folder = f"{rootdir}/{work_folder}-{i:02d}/submission/"
    print(f"In {submission_folder}")
    if os.path.isdir(submission_folder):
        if os.path.isfile(f"{submission_folder}/team.json"):
            with open(f"{submission_folder}/team.json", "r") as f:
                team_info = json.load(f)
                teamname = team_info["name"]
                members = ";".join(team_info["members"])

            submission_file = f"{submission_folder}/{teamname}_eval_submission.csv"
            if os.path.isfile(f"{submission_file}"):
                # read submission files
                df_submission = pl.read_csv(
                    submission_file,
                ).with_columns(pl.all().cast(pl.Int64))

                df_submission = df_submission.sort(["year", "idnum", "month"])

                # score computation
                df_match = df_eval.join(
                    df_submission,
                    on=["year", "month", "idnum"],
                    how="left",
                    suffix="_submission",
                ).sort(["year", "idnum", "month"])
                d = df_match.with_columns(
                    (pl.col("vg_statebus") == pl.col("vg_statebus_submission"))
                    .alias("vg_statebus_match")
                    .cast(pl.Int16),
                    (pl.col("vg_comexp") == pl.col("vg_comexp_submission"))
                    .alias("vg_comexp_match")
                    .cast(pl.Int16),
                    (pl.col("vg_priceexp") == pl.col("vg_priceexp_submission"))
                    .alias("vg_priceexp_match")
                    .cast(pl.Int16),
                ).select(
                    pl.col(
                        ["vg_statebus_match", "vg_comexp_match", "vg_priceexp_match"]
                    ).sum()
                    / len(df_eval)
                )

                score = d.mean(axis=1).alias("score").to_numpy()[0]

                df = pl.DataFrame(
                    data={"team": teamname, "members": members, "score": score}
                )
                df_list.append(df)


if df_list:
    final_scores_df = pl.concat(df_list)
    final_scores_df.write_csv("scores.csv", has_header=True)
