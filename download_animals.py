#!/usr/bin/env pyhon3
import os
import shutil
import urllib

iconList = ('Alligator', 'Anteater', 'Armadillo', 'Auroch', 'Axolotl', 'Badger', 'Bat', 'Bear', 'Beaver', 'Buffalo', 'Camel', 'Capybara', 'Chameleon', 'Cheetah', 'Chinchilla', 'Chipmunk', 'Chupacabra', 'Cormorant', 'Coyote', 'Crow', 'Dingo', 'Dinosaur', 'Dog', 'Dolphin', 'Duck', 'Elephant', 'Ferret', 'Fox', 'Frog', 'Giraffe', 'Gopher', 'Grizzly', 'Hedgehog', 'Hippo', 'Hyena', 'Ibex','Ifrit', 'Iguana', 'Jackal', 'Kangaroo', 'Koala', 'Kraken', 'Lemur', 'Leopard', 'Liger', 'Lion', 'Llama', 'Loris', 'Manatee', 'Mink', 'Monkey', 'Moose', 'Narwhal', 'Nyan Cat', 'Orangutan', 'Otter', 'Panda', 'Penguin', 'Platypus', 'Pumpkin', 'Python', 'Quagga', 'Rabbit', 'Raccoon', 'Rhino', 'Sheep', 'Shrew', 'Skunk', 'Squirrel', 'Tiger', 'Turtle', 'Walrus', 'Wolf', 'Wolverine', 'Wombat')

dirname = 'icons'
if os.path.exists(dirname):
    shutil.rmtree(dirname)
os.makedirs(dirname)

for index, icon in enumerate(iconList):
    filename = dirname + '/' + icon + '.png'
    print('#%s\tfetching %s' % (index, filename))
    url = 'https://ssl.gstatic.com/docs/common/profile/' + icon + '_lg.png'
    urllib.urlretrieve(url, filename)

# TODO: write all icons to index.html