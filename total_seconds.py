# Convert hours, minutes and seconds into total seconds
# example total_seconds(1, 1, 1) => 3600+60+1 = 3661
def total_seconds(hours, minutes, seconds):
  # write some code and return the result
  return hours * 3600 + minutes *60 + seconds

print(total_seconds(5, 0, 0))