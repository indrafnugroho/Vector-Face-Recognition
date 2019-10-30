def show_img(path):
    img = imread(path, mode="RGB")
    plt.imshow(img)
    plt.show()
    
def run():
    images_path = 'resources/images/'
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    # getting 3 random images 
    sample = random.sample(files, 3)
    
    batch_extractor(images_path)

    ma = Matcher('features.pck')
    
    for s in sample:
        print 'Query image =========================================='
        show_img(s)
        names, match = ma.match(s, topn=3)
        print 'Result images ========================================'
        for i in range(3):
            # we got cosine distance, less cosine distance between vectors
            # more they similar, thus we subtruct it from 1 to get match value
            print 'Match %s' % (1-match[i])
            show_img(os.path.join(images_path, names[i]))

run()