if [ $# -ne 2 ]; then
  echo "Usage: $0 <SH_snid> <out_dir>"
  echo "E.g.: $0 ~/Downloads/SH_snid.csv/SH_snid.csv ."
  echo "Collect names and surnames from BIN.";
  exit 1;
fi

SH_snid=$1
DEST=$2
FALL="NFET"

cat $SH_snid | grep ";móð;\|;föð;" | grep "dóttir;" | grep ";$FALL" | cut -f5 -d";" > $DEST/surnames_kvk.txt
cat $SH_snid | grep ";móð;\|;föð;" | grep "son;" | grep ";$FALL" | cut -f5 -d";" > $DEST/surnames_kk.txt
cat $SH_snid | grep ";ism;" | grep ";kvk;" | grep ";$FALL" | cut -f5 -d";" > $DEST/names_kvk.txt
cat $SH_snid | grep ";ism;" | grep ";kk;" | grep ";$FALL" | cut -f5 -d";" > $DEST/names_kk.txt

