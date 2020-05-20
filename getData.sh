function download(){
    a='https://s3-eu-west-1.amazonaws.com/public.bitmex.com/data/trade/'
    date=$1
    full_url="${a}${date}.csv.gz"
    file_compressed="${date}.csv.gz"
    file="${date}.csv"
    axel -n 10 $full_url
    gunzip $file_compressed
    mv ${file} data
}
function runIt(){
    filePath=data/${1}.csv
    echo "$filePath"
    if test -f "$filePath"; then
        echo "file found"
    else
        download $1
    fi
    python createDf.py ${1}.csv
    rm $filePath

}

dates=()
startdate=20181231
enddate=20200101
d=$start
n=0
until [ "$d" = "$enddate" ]
do  
    ((n++))
    d=$(date -d "$startdate + $n days" +%Y%m%d)
    dates+=("$d ")
    # echo $d
done
echo "${dates[@]}"
# dates="20200111 20200115 20200118 20200123 20200126 20200201 20200202 20200203 20200206 20200208 20200219 20200223 20200228 20200308 20200416"
# dates="20200105 20200106"
for date in "${dates[@]}"
do
  runIt $date
done
# runIt "20200103"

