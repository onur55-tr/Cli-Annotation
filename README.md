# cli_for_annotation

## HOW TO WORK

The work was done with two annotators who annotated main.txt, which splits it into true and false categories. After that cross-examination is done to spot differences in annotation.

1. To start annotating first run this command:
~~~python
python3 cli.py
~~~
2. After annotation is done run this command to create json file for future cross-examination (do you agree or disagree with other annotators choice?):
~~~python
python3 create_json.py <folder path to your annotation folder>
~~~
3. To start cross-examination with other annotator run:
~~~python
python3 diff.py
~~~

    -rw-rw-r-- 1 odursun  2021_istanbul  35149 Jul 25 22:34 LICENSE
    -rw-rw-r-- 1 odursun  2021_istanbul    689 Jul 25 22:34 README.md
    drwxrwxr-x 4 odursun  2021_istanbul    136 Jul 25 22:34 annotation_files
    -rw-rw-r-- 1 odursun  2021_istanbul   3893 Jul 25 22:34 cli.py
    -rw-rw-r-- 1 odursun  2021_istanbul    990 Jul 25 22:34 create_json.py
    -rw-rw-r-- 1 odursun  2021_istanbul   2619 Jul 25 22:34 diff.py
    drwxrwxr-x 4 odursun  2021_istanbul    136 Jul 25 22:34 first_annotator
    -rw-rw-r-- 1 odursun  2021_istanbul     17 Jul 25 22:34 requirements.txt
    drwxrwxr-x 4 odursun  2021_istanbul    136 Jul 25 22:34 second_annotator
    drwxrwxr-x 3 odursun  2021_istanbul    102 Jul 25 22:34 statistics



```python

$ Operating System : MacOS

*************** Directory Tree ***************

CLI for Annotation/
├──LICENSE
│
│
├── README.md
│
│
├── annotation_files/ # MAIN
│   └── first_pass/
│       ├── false.txt
│       ├── false.txt
│       ├── false.txt
│
│   └── second_pass
│       ├── false.txt
│       ├── false.txt
│       ├── false.txt
│
│
├── cli.py # Annotation program
│
│
├── create_json.py # Converting true and false txts to json extension
│
│
├── diff.py # evaulation
│
│
├── first_annotator/ # ABDULSELAM
│   └── first_pass/ # DATASET-1
│       ├── agree.txt
│       ├── cursor.txt
│       ├── cursor_backuptxt
│       ├── disaggre.txt
│       ├── false.json
│       ├── false.txt
│       ├── true.json
│       ├── true.txt
│
│   └── second_pass/ # DATASET-2
│       ├── agree.txt
│       ├── cursor.txt
│       ├── cursor_backuptxt
│       ├── disaggre.txt
│       ├── false.json
│       ├── false.txt
│       ├── true.json
│       ├── true.txt
│
│
├── requirements.txt
│
│
├── second_annotator/ # ONUR
│   └── first_pass/ # DATASET-1
│       ├── agree.txt
│       ├── cursor.txt
│       ├── cursor_backuptxt
│       ├── disaggre.txt
│       ├── false.json
│       ├── false.txt
│       ├── true.json
│       ├── true.txt
│
│   └── second_pass/ # DATASET-2
│       ├── agree.txt
│       ├── cursor.txt
│       ├── cursor_backuptxt
│       ├── disaggre.txt
│       ├── false.json
│       ├── false.txt
│       ├── true.json
│       ├── true.txt
│

```

```
@article{DBLP:,
  author    = {Onur Dursun && Abdulselam Karahan && Emrecan && Deniz Yuret},
  title     = {MorphNet: {A} sequence-to-sequence model that combines morphological analysis and disambiguation},
  journal   = {CoRR},
  volume    = {},
  year      = {2022},
  url       = {},
  archivePrefix = {arXiv},
  eprint    = {},
  timestamp = {Mon, 13 Aug 2018 16:47:09 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1805-07946},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

|trmor2018	|train	|
|-----------|-------|
|Documents	|390	|
|Sentences	|34673	|
|Tokens 	|460669	|
|Unambiguous|243866	|
|Ambiguous	|215024	|
|Unknown	|1779	|


## Developers

![Onur55-tr](https://github.com/onur55-tr.png?size=100) | ![A-karah](https://github.com/a-karah.png?size=100)
----|----|
| [Onur Dursun](https://github.com/onur55-tr) | [Abdulselam Karahan](https://github.com/a-karah)
Developer, Base, Bug Fixes, Modules | Author, Developer, Base, Bug Fixes, Modules

## License
This project is protected by `GNU General Public Licence v3.0` license.
