# Plant supplier SAP Codes
The parameter list file is an index of the plant supplier SAP codes. This is specially useful for purchasing assistants and buyers to understand which SAP system belongs each plant for the purpose of creation of master data, scheduling lines, price changes, etc. The original file is maintained manually with the latest update being 2023/04. The code generates a prefect workflow to update plant supplier SAP codes daily using a cron scheduler.

## Output format

| Plant | Address | City | Purchasing Group | Country | Plant Name | Business Unit | SAPSYS |
|-------|---------|------|------------------|---------|------------|---------------|--------|
|       |         |      |                  |         |            |               |        |

## Results

- From 133 plant numbers in the legacy file to 962 plant numbers in this improved file
- The file is now up-to-date with the latest T001W_* Plants/Branches data SAP view and does not need to be updated manually
- File maintained every day with cron scheduling
