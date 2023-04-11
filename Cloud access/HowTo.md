# Kick-ass tutorial on the GCP Workflow

## Prerequisites

### Usernames and passwords
Your usernames, in the format User**XX**-ifohack2023@ifo.de, will be provided to you by us. You will also receive a password along with your username that you will use to access the GCP. In addition, you will also get access to your personal VM and a link will be provided to you, in the format https://console.cloud.google.com/compute/instances?cloudshell=true&orgonly=true&project=vo-ifohack2023-work-prod-**XX**

### Browser/Extensions
You **need** to use Google Chrome in order to get the GCP working. In addition, you also need [Chrome Remote Desktop](https://chrome.google.com/webstore/detail/chrome-remote-desktop/inomeogfingihgjfjlpeplalcfajhgai).

## Logging in for the first time

### Setting up 2FA
Once you log-in for the first time, you will be ask to set up 2FA. You can use the Authenticator app ([iOS](https://apps.apple.com/de/app/microsoft-authenticator/id983156458), [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator&hl=de&gl=US&pli=1)) to set up 2FA.

### Dashboard
Your dashboard should look like the following:
![image](https://user-images.githubusercontent.com/44307642/228552957-295b0b73-4c3a-4a83-a562-bd557f5592f1.png)
Make sure that both machines are running (green ticks). If this is not the case contact XXXXX.

### SSH connection
#### Starting SSH connection
In order to access the VM, you need to start a SSH connection with jump-vm and use the [Chrome Remote Desktop App](https://remotedesktop.google.com/access).

![ssh_connection](https://user-images.githubusercontent.com/44307642/229470086-e92e99ac-1ebc-46ba-8777-8089c458f899.gif)

#### Copy SSH key
After clicking on the SSH connection in GCP, keep the window opened, use the Chrome Remote Desktop App and set up a new SSH connection on the left hand side. After clicking through the steps, copy the Debian Linux section (starts with ```DISPLAY...```). 

![chrome desktop](https://user-images.githubusercontent.com/44307642/229471429-9aebcfa2-f035-41dd-aaaf-f66cdb514225.gif)

#### Creating your own PIN
Paste the block to the previously opened ```ssh.cloud.google.com``` window. If it was successful, you are prompted to enter a PIN of at least six digits. 

![image](https://user-images.githubusercontent.com/44307642/229472546-ffb7dcfe-e494-4602-bb23-3cea17b9c049.png)

Once you are done with this step, you should be able to see the ```jump-vm-prod-xx``` as online in remotedesktop.google.com/access

![image](https://user-images.githubusercontent.com/44307642/229472760-b2ab0736-4341-4abb-aa6f-3a13b907302b.png)

#### Accessing your GUI
You can now access the jump-vm. You just have to enter the PIN that you previously created and then click on connect, such that you will be connected to the GUI of the work-vm. 

![jump-vm-connection](https://user-images.githubusercontent.com/44307642/229474337-9a404d85-db24-4236-8805-d9d79e7c077a.gif)


#### Creating a `conda` environment
From the admin-vm create a conda environment with `conda create --prefix <path-to-new-env> python pip <any-other-packages>` or if you have a conda environment file, say `environment.yml`, run `conda env create -f environment.yml`.

Then zip and copy the created environment directory to the work-vm `sourcedata` folder, e.g. `work-vm-prod-01`.

##### Install the packages on the work-vm

From the work-vm, copy the zipped conda packages from `sourcedata` to `~/Desktop/project-directory/env`, then unzip it. In the terminal of the work-vm, run `conda activate <path-to-env-dir>`, to activate the new conda environment, or just copy the code block below:

```sh
unzip source-data/<new-env>.zip -d ~/Desktop/project-directory/env
conda activate ~/Desktop/project-directory/env/<new-env>
```

That's it! That's your working environment for the ifoHack!



