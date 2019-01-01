# The user has to specify the numnber to start from and end to
# Also the amount by which to count

start = int(input("Please enter the start of the counter"))
end = int(input("Please enter the end of the counter"))
diff = int(input("Plese enter the amount by which the counter should move"))

for i in range(start,end+1,diff):
    print(i,end = ' ')