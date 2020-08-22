# Tachiyomi-details.json-generator
This python scripts help manually make the details.json for Tachiyomi local manga
using the format as shown at [Reading local manga](https://tachiyomi.org/help/guides/reading-local-manga/#archive-files)


>>Steps:
1. Run the script on any Python 3 compiler

2. Enter the info as prompted

3. If details.json not existed beforehand, it should be now. Otherwise, new info is overwrited onto it.

Note:
  >> Description prompt currently cannot be entered with line break.
      For example, this will not work:
      
        "This is the 1st paragraph... blah blah......
      
          This is the 2nd paragraph ....blah blah......."
  >> Genre should enter in the format:
        genre1, genre2, ..., genreN
