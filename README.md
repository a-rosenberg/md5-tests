# md5 Multithread Speed Tests

### Structure
- main calls in `md5.py`
- place target data in static/data directory
- `python md5.py`

### Results
#### stdout
```
/Users/arosenbe/anaconda2/bin/python /Users/arosenbe/Projects/md5_timing/md5.py
INFO:root:`serial_md5` execution time: 2.5557179451
INFO:root:`threaded_md5` execution time: 0.690050125122

Process finished with exit code 0

```
#### static/test.md5
```5e20db17c2f3d178a394c3189f781b4b static/data/Atlantic_line_612patch.all.mb58.gz
c1cb17ce8f4197d9f49b2ba025f53983 static/data/Atlantic_line_616tran.all.mb58.gz
8537c4cd55e033d7b8d6038e4fb269b9 static/data/Atlantic_line_617.all.mb58.gz
bcaf57a520b102919411cf0f482b4d90 static/data/Atlantic_line_675.all.mb58.gz
bf712df72b315485dab503ce91309a86 static/data/Atlantic_line_676.all.mb58.gz
5a6590dea50f52db7117e9e171f8f39a static/data/Atlantic_line_679.all.mb58.gz
cf4bc81941af100ec97476f27bda05da static/data/Atlantic_line_684.all.mb58.gz
801f22c8e6675b96a73a7a9cbcc41d79 static/data/Atlantic_line_686.all.mb58.gz
2c4d2273bc9c136b4b179ed545ab1d09 static/data/Atlantic_line_695tran.all.mb58.gz
914064a2b48fec128edc84bae112918b static/data/Atlantic_line_701.all.mb58.gz
6a677e3bfaef5493464d9e09a62393e3 static/data/Atlantic_line_702.all.mb58.gz
0ef5e6044e7b4f4db1d05dc5e0c14cb6 static/data/Atlantic_line_704.all.mb58.gz
59c62e469b5fb52501a44edd7c8ea64c static/data/Atlantic_line_710.all.mb58.gz
52117b8eb946195758ae549551642308 static/data/Atlantic_line_713.all.mb58.gz
b0fa41caee4c4166c21f7c31690bdd6d static/data/README.md
```
