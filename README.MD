# Plant supplier SAP Codes
The parameter list file is an index of the plant supplier SAP codes. This is specially useful for purchasing assistants and buyers to understand which SAP system belongs each plant for the purpose of creation of master data, scheduling lines, price changes, etc. The original file is maintained manually with the latest update being 2023/04. The code generates a prefect workflow to update plant supplier SAP codes daily using a cron scheduler.

## Output format

| Plant | Address | City | Purchasing Group | Country | Plant Name | Business Unit | SAPSYS |
|-------|---------|------|------------------|---------|------------|---------------|--------|
|       |         |      |                  |         |            |               |        |

## Results

- From 133 to 962 plant numbers
- The file is up-to-date with the latest T001W_* Plants/Branches data SAP view
- File maintained every day with cron scheduling
