#!/usr/bin/env python

import ROOT
import numpy as n

print "Writing a tree"

f = ROOT.TFile("tree.root", "recreate")
t = ROOT.TTree("hits", "Energy Deposits in Detector")
t2 = ROOT.TTree("events", "Events of Energy deposits")


MAX_HITS = 10000
# create 1 dimensional float arrays (python's float datatype corresponds to c++ doubles)
# as fill variables
x = n.zeros(1, dtype=float)
y = n.zeros(1, dtype=float)
z = n.zeros(1, dtype=float)
en = n.zeros(1, dtype=float)

nhits = n.zeros(1, dtype=int)
xs = n.zeros(MAX_HITS, dtype=float)
ys = n.zeros(MAX_HITS, dtype=float)
zs = n.zeros(MAX_HITS, dtype=float)
ens = n.zeros(MAX_HITS, dtype=float)

event = n.zeros(1, dtype=int)

# create the branches and assign the fill-variables to them
t.Branch('event', event, 'event/I')
t.Branch('x', x, 'x/D')
t.Branch('y', y, 'y/D')
t.Branch('z', z, 'z/D')
t.Branch('en', en, 'en/D')


t2.Branch('event', event, 'event/I')
t2.Branch('nhits', nhits, 'nhits/I')
t2.Branch('x', xs, 'x[nhits]/D')
t2.Branch('y', ys, 'y[nhits]/D')
t2.Branch('z', zs, 'z[nhits]/D')
t2.Branch('en', ens, 'en[nhits]/D')

r = ROOT.TRandom3()
for ev in range(10):
   event[0] = ev
   radius = r.Uniform(2,10)
   x_avg = r.Gaus(0,10)
   y_avg = r.Gaus(0,10)
   z_start = r.Uniform(-10,10)
   z_length = r.Uniform(1,20)
      
   N = 1000
   nhits[0] = int(r.Gaus(N, ROOT.TMath.Sqrt(N)))
   for hit_n in range(nhits[0]):
      x[0] = r.Gaus(x_avg,radius)
      y[0] = r.Gaus(y_avg,radius)
      z[0] = r.Uniform(z_start,z_start + z_length)
      rad = ROOT.TMath.Sqrt((x[0] - x_avg)**2 + (y[0] - y_avg)**2)
      en[0] = 100*ROOT.TMath.Exp(-rad/radius) * ROOT.TMath.Exp(- 3.0*( z[0] - z_start)/ z_length)
      xs[hit_n] = x[0]
      ys[hit_n] = y[0]
      zs[hit_n] = z[0]
      ens[hit_n] = en[0]
      t.Fill()
   t2.Fill()


# write the tree into the output file and close the file
f.Write()
f.Close()
