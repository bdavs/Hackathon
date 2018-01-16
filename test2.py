import datetime
import sys
 
master = Tk()
 
e = Entry(master)
e.pack()
 
e.focus_set()
 
def callback():
    print (e.get())
 
b = Button(master, text="get", width=10, command=callback)
b.pack()
 
mainloop()
e = Entry(master, width=50)
e.pack()
 
text = e.get()
def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry
 
hour = makeentry(parent, "Hour", 10)
minute = makeentry(parent, "Minute", 10)
second = makeentry(parent, "Second", 10)
day = makeentry(parent, "Day", 10)
month = makeentry(parent, "Month", 10)
year = makeentry(parent, "Year", 10)
millisecond = makeentry(parent, "Millisecond", 10)
content = StringVar()
entry = Entry(parent, text=caption, textvariable=content)
 
text = content.get()
content.set(text)
 
#datetime.datetime.now()
#datetime(year, 1, 6, 15, 8, 24, 78915)
 
 
 
time_tuple = ( year, # Year
                  month, # Month
                  day, # Day
                  hour, # Hour
                 minute, # Minute
                  second, # Second
                  millisecond, # Millisecond
              )
 
def _win_set_time(time_tuple):
    import pywin32
    # http://timgolden.me.uk/pywin32-docs/win32api__SetSystemTime_meth.html
    # pywin32.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )
    dayOfWeek = datetime.datetime(time_tuple).isocalendar()[2]
    pywin32.SetSystemTime( time_tuple[:2] + (dayOfWeek,) + time_tuple[2:])
 
 
def _linux_set_time(time_tuple):
    import ctypes
    import ctypes.util
    import time
 
    # /usr/include/linux/time.h:
    #
    # define CLOCK_REALTIME                     0
    CLOCK_REALTIME = 0
 
    # /usr/include/time.h
    #
    # struct timespec
    #  {
    #    __time_t tv_sec;            /* Seconds.  */
    #    long int tv_nsec;           /* Nanoseconds.  */
    #  };
    class timespec(ctypes.Structure):
        _fields_ = [("tv_sec", ctypes.c_long),
                    ("tv_nsec", ctypes.c_long)]
 
    librt = ctypes.CDLL(ctypes.util.find_library("rt"))
 
    ts = timespec()
    ts.tv_sec = int( time.mktime( datetime.datetime( *time_tuple[:6]).timetuple() ) )
    ts.tv_nsec = time_tuple[6] * 1000000 # Millisecond to nanosecond
 
    # http://linux.die.net/man/3/clock_settime
    librt.clock_settime(CLOCK_REALTIME, ctypes.byref(ts))
 
 
if sys.platform=='linux2':
    _linux_set_time(time_tuple)
 
elif  sys.platform=='win32':
    _win_set_time(time_tuple)
