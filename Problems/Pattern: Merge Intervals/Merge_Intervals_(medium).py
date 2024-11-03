  def merge(self, intervals):
    mergedIntervals = []

    intervals.sort(key=lambda x: x.start)

    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
      
      if intervals[i].start <= end:
        end = max(intervals[i].end, end)
      else:
        mergedIntervals.append([start, end])
        start = intervals[i].start
        end = intervals[i].end
    
    mergedIntervals.append([start, end])

    return mergedIntervals
