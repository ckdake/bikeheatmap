import heatmap # http://jjguy.com/heatmap/
import random
import csv

if __name__ == "__main__":
    pts = []
    for point in csv.reader(open('coords.csv')):
      pts.append((float(point[0]), float(point[1])))

    print "Processing %d points..." % len(pts)

    hm = heatmap.Heatmap()
    hm.heatmap(pts, "heatmap.png", 25, 128, (8192,8192))
    hm.saveKML("heatmap.kml")
