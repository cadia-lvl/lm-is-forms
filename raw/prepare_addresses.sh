if [ $# -ne 3 ]; then
  echo "Usage: $0 <Staðfangaskra> <postnumer> <out_dir>"
  echo "E.g.: $0 Stadfangaskra.csv postnumer.txt ."
  echo "Prepare data to generate addresses.";
  exit 1;
fi

STAD=$1
POST=$2
DEST=$3
STADT=Stadfangaskra.tsv
python csv2tsv.py $STAD > $STADT
tail -n +2 $POST | cut -f1 -d";" | grep "\S" > $DEST/postnumer.lst
tail -n +2 $POST | cut -f2 -d";" | grep "\S" > $DEST/city.lst
tail -n +2 $STADT | cut -f9 -d"	" | sort | uniq | grep "\S" > $DEST/street_nf.lst 
tail -n +2 $STADT | cut -f10 -d"	" | sort | uniq | grep "\S" > $DEST/street_tgf.lst 
tail -n +2 $STADT | cut -f11 -d"	" | sort -n | uniq | grep "\S" > $DEST/house_number.lst 
