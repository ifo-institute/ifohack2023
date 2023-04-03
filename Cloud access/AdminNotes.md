## Administrator How-To

1. Access https://console.cloud.google.com/ through @ifo.de domain, 2FA
2. Open the console, select `vo-ifohack2023-admin-prod-01`
3. Navigate to Cloud storage, Buckets: prod-sourcedata *all changes to the dataset must go here and are copied to the work-vms*
4. Locate work-vm, IBS (**don't download!**)
		- `10-7805_ebdc-ibs-con-2022b.csv` (con)
		- `10-7805_ebdc-ibs-ind-2022b.csv` (industrial production)
		- `10-7805_ebdc-ibs-serv-2022b.csv` (services)
		- `10-7805_ebdc-ibs-tra-2022b.csv` (trade)
5. Navigate to Compute Engine (**don't touch `gitea`**)
6. Start/Stop `admin-prod-01` (type is `e2-standard-4` without GPU)
7. Select `SSH` button
8. Open Chrome Remote Desktop
9. Establish connection (paste Linux command)
10. Copy/paste `source-data` manually to individual work-vms
