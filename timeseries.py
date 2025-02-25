solo_mag = TimeSeries(downloaded_files, concatenate=True)
print(solo_mag.columns)
solo_mag.peek(columns=['B_RTN_0', 'B_RTN_1', 'B_RTN_2'])
