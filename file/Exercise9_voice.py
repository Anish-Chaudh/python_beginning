import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
l = ["Rahul","Anish","Amrit","Mahesh","santosh","saroj","susmita","Aakriti","Ranjana","saru","sostika","saroj"]
for i in range(0, len(l)):
    s = "shout out to " + l[i]
    print(s)
    speaker.Speak(s)