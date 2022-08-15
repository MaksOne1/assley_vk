

import os
from Image import ImageParser


ReMangaSettings = {
    'headers': {
        'authorization': 'bearer eDKxOWWo9rD3Rr5U6mRkRf3MAdj39l'
    },
    'branch': 'https://api.remanga.org/api/titles/chapters/?branch_id={branch}&count=60&ordering=-index&page={page}'
}

image_parser = ImageParser()
# image_parser.download('test', 1, [
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/85ad2027f5d5beba3891aa60c62ca150.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/999b3d2d2a1da6d1bf59d378fba15d62.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/739f4027d31e071b0b6dc2a2465698e1.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/508a61f93e8f5e943a10b3d50bf69a0c.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/19318dbb85b5839ef9037468d01403f2.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/293b16da10e5ca8c1e46005b4874e367.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/f6d55b55069b9c017556dd93b50cdd0f.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/ec59c21b6ea34c2196229d76d1cd10d2.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/c128548f8ccb98ae90603c95240a4438.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/84755b4d379f1032843e2617fa9cd0dd.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/c7b2a16a5b53fa70de3434ec807d73b9.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/436da937703f83da82b534207ee407e5.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/b78b6a66f921abc57fbefe71c1ee3731.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/765f78e9a1efb8d69e32af5be025801f.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/fb644e86f5228b0c225c55b65ca8083b.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/e2f3f3d70e5cbeb04b65a516c9c85e1c.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/89d2a52bf9e1d82c3812a4726cdb5843.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/c69db12c3ca860b0c5b3496719766b88.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/081e77ebb5a75aab1f853087b65c3aa3.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/ae28a91618b131cb696c8e67b05a5150.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/b0366eeae58bde331bee491c7c7b5a4e.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/74f2f33a45370a7a9eccc35775e3b8f9.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/80730a6874dad174b411bd1230cff481.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/04d354e2583277799203ebfeba15e00b.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/bc9ed4cd5c1c1ee824c30607201942a1.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/1c239692d2850916aa4192f6ede54386.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/9911e0c13c8950c17ba4a96ec12becea.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/a0efccef928cf3b0eaf0e568c8c4d95c.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/6344b954fce3e87279e4024c67a43005.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/e79beb0ba832e9f83a432de63982628d.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/d5e86fcf026345fc892084b2b840392a.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/681eab370edd1b3a5ba15277753ac1be.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/c031ddce47ce2e26d067f3c4ec139d67.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/3aa563285e00e0e10811f5d54f1708cc.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/d2b3d0ee53a7f9b97a9f099dd642fb82.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/c2af032c2c1b10a0205a89ff9b94bb50.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/8f26b9827a008a08c5324e1bc5bd639a.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/012e41f50558f5182d974c38d9e5e838.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/8a8ddc8d67ecd4e278f7eddf495f8d85.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/7a20c278e72a973cfdf8239d85209dfe.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/894ae29364c0316fd7a093fdf5ddb375.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/43106458c7572b20802516e8586e1e8b.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/0de3ca18035860d40572bbab32a13b89.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/5e2e0da364ff3861f3d0fdbf98c847cc.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/5698b3a91287f65e637b3a277312a5df.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/64d9b4a45d43a0f96d322859881546fa.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/a0e6f95932feb0d513e87321682b7c1e.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/6c96827b08bd42b8880467e03f4bf65b.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/a38560b1aee96b7226dec6b55c41d102.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/95c3d56f119d73f14480efd7f26336bc.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/7e18b1112db5784188890db3bb01301c.jpeg",

#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/1cd7d6e5de2e456a6d146dc9e0bb2554.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/6ffdb9fb23fe1f1a97c6b68c36ceb534.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/ed47582a6ca4769d9fab27b667784458.jpeg",
#     "https://img2.reimg.org/images/player-who-returned-10000-years-laters/3ea84f6cbb34e34e45ec77208a21594c/8d36ec4cc782b753c24e1f9833924a2e.jpeg"
# ])
path = os.path.join(__file__, '..', 'assets', 'test', '1')
file = image_parser.join('test', 1, [os.path.join(path, x) for x in os.listdir(path)])
image_parser.slice(
    '0concat.jpg', 'c:\\Users\\Максим\\Desktop\\chapter_downloader_bot\\Image.py\\..\\assets\\test\\concat\\1\\', 2000)
# ['c:\\Users\\Максим\\Desktop\\chapter_downloader_bot\\Image.py\\..\\assets\\test\\concat\\1\\0concat.jpg', 'c:\\Users\\Максим\\Desktop\\chapter_downloader_bot\\Image.py\\..\\assets\\test\\concat\\1\\1concat.jpg', 'c:\\Users\\Максим\\Desktop\\chapter_downloader_bot\\Image.py\\..\\assets\\test\\concat\\1\\2concat.jpg']