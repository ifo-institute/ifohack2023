#import required libraries

from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

#print the code below
with st.echo(code_location='below'):
   #print a slider with minimum value of 0, maximum value 500 and standard value of 2000
   total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
   num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

   Point = namedtuple('Point', 'x y')
   data = []

   points_per_turn = total_points / num_turns

   for curr_point_num in range(total_points):
      curr_turn, i = divmod(curr_point_num, points_per_turn)
      angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
      radius = curr_point_num / total_points
      x = radius * math.cos(angle)
      y = radius * math.sin(angle)
      data.append(Point(x, y))

   #print a chart with the data instances made from in the code above
   #for more details check: https://docs.streamlit.io/library/api-reference/charts/st.altair_chart
   st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
      .mark_circle(color='#0068c9', opacity=0.5)
      .encode(x='x:Q', y='y:Q'))