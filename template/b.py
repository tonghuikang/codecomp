class StarsInTheSky:
    def countPictures(self, n, xx, yy):
        pictures = set()
       	for x1 in xx:
            for y1 in yy:
                for x2 in xx:
                    for y2 in yy:
                        stars = []
                        for x,y in zip(xx,yy):
                            if x1 <= x <= x2 and y1 <= y <= y2:
                                stars.append((x,y))
                        if stars:
                            pictures.add(tuple(stars))
        
        return len(pictures)