import ROOT

f = ROOT.TFile.Open("tree.root")


print "output first 10 hits for each event using 'hits'"
hits = f.Get("hits")
last_event = -1
for hit in hits:
   if hit.event is not last_event:
      i = 0
   if i >= 10: continue
   print hit.event, hit.x, hit.y, hit.z, hit.en
   last_event = hit.event
   i += 1

print "output first 10 hits for each event using 'events'"
events = f.Get("events")
for event in events:
   for i in range(10):
      print event.event, event.x[i], event.y[i], event.z[i], event.en[i]


# TTree.Draw() takes 3 arguments, 1st tells it what to draw, 1d plot "x", 2d plot "x:y", 3d plot "x:y:z"
# 2 argument is a 'cut' string. If it evaluates to zero, that entry is not plotted. if it is a float, its plotted with that weight. 
# 3rd argument is the draw options. https://root.cern.ch/doc/master/classTHistPainter.html#HP01

print "draw energy deposits in x-y plane"
hits.Draw("x:y","en*(event==0)", "colz")

print "works the same for 'events' tree"
events.Draw("x:y","en*(event==0)", "colz")


print [sum(event.en) for event in events]
