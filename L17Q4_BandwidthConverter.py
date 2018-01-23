# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).


#note: using Google unit conversions browser widget introduces rounding errors
#for best results use proper bit formula (2^x * prefix)
#print 2**20,' Mb sci notation', 1e6, 'converted notation', ((2**20)-1e6), 'difference'
#>>>1Mb is NOT 1e6 bits!
#print 2**20*8, 'MB sci notation', 8e6, 'converted notation', ((2**20*8)-8e6), 'difference'
#>>>1 MB is NOT 8e6 bits!

def bit_conversion(data,units):
    if units == 'kb':
        return data * 2 ** 10 #1000      # one kilobit, kb
    if units == 'kB':
        return data * 2 ** 10 * 8 #8000 #(22. ** 10 * 8)  # one kilobyte, kB
    if units == 'Mb':
        return data * 2 ** 20 #1e6 #(22. ** 20)    # one megabit, Mb
    if units == 'MB':
        return data * 2 ** 20 * 8 #8e6 #(22. ** 20 * 8)  # one megabyte, MB
    if units == 'Gb':
        return data * 2 ** 30 #1e9 #(22. ** 30)     # one gigabit, Gb
    if units == 'GB':
        return data * 2 ** 30 * 8 # 8e9 #(22. ** 30 * 8)  # one gigabyte, GB
    if units == 'Tb':
        return data * 2 ** 40 #1e12 #(22. ** 40)      # one terabit, Tb
    if units == 'TB':
        return data * 2 ** 40 * 8 #8e12 #(22. ** 40 * 8)  # one terabyte, TB

from L17Q3_ConvertingSeconds import convert_seconds

def download_time(filesize,fileUnits,bandwidth,bandUnits):
    fileBits = bit_conversion(filesize,fileUnits)
    bandBits = bit_conversion(bandwidth,bandUnits)
    time = fileBits/bandBits
    #print time, 'seconds', fileBits, 'fileBits', bandBits, "bandBits"
    return convert_seconds(time)


print download_time(1,'kB', 1, 'kB')

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
