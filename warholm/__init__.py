import untangle, urllib

def getting_data():
    url = 'http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml'
    doc = untangle.parse(urllib.urlopen(url).read())

    reason = [outage.reason.cdata for outage in doc.NYCOutages.outage]
    print float(reason.count('REPAIR'))/float(len(reason)) 
