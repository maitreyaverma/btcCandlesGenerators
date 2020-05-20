# Bitcoin candle generator
Will fetch the public data from bitmex of trades for each day and convert them to 1 min candles.
## Usage
In getdata.sh, there is startdate and enddate variables. Change them according to the need. 
Also, have to create a temp folder named data/, candles/1h and candles/1min. This is where the candles are stored. 
If interested, can run it for all dates in parallel. Just edit the line 41 to 
```
  runIt $date &
```