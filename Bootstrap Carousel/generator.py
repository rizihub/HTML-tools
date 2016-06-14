from os import listdir

#/Users/Rizi/Pictures/Funny

directory = input("Enter directory: ")
dirList = []
dirList = listdir(directory)

wantedItems = []

for f in dirList:
	if ".jpg" in f or ".png" in f:
		wantedItems.append(f)

count = len(wantedItems)


firstLine = '<div id="myCarousel" class="carousel slide" data-ride="carousel">'
lastLine = '</div>'


#create the indicators
def generateIndicators(count):
	first = '<ol class="carousel-indicators">\n'
	middle = '<li data-target="#myCarousel" data-slide-to="0" class="active"></li>\n'
	if(count > 1):
		for i in range(1, count):
			middle = middle + '<li data-target="#myCarousel" data-slide-to="' + str(i) + '"></li>\n'

	end = '</ol>\n'
	return first + middle + end

#Wrapper
def generateWrapper(count):
	first = '<div class="carousel-inner" role="listbox">\n'
	div1 = '<div class="item active">\n<img src="' + wantedItems[0] + '" alt="">\n</div>'
	otherDivs = ""
	if(count > 1):
		for i in range(1, count):
			otherDivs = otherDivs + '<div class="item">\n<img src="' + wantedItems[i] + '" alt="">\n</div>\n'
	return first + div1 + otherDivs + '</div>\n'

#left right controls
def generateControls():
	return '<a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">\n<span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>\n<span class="sr-only">Previous</span>\n</a>\n<a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">\n<span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>\n<span class="sr-only">Next</span></a>\n'


final = firstLine + generateIndicators(count) + generateWrapper(count) + generateControls() + lastLine

print(final)
