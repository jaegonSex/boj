import sys
class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self._insert(self.root,data)
        return self.root is not None
    def _insert(self,node,val):
        if node is None:
            node=Node(val)
        else:
            if val<=node.data:
                node.left=self._insert(node.left,val)
            else:
                node.right=self._insert(node.right,val)
        return node

    def max(self):
        now = self.root
        while now.right:
            now = now.right
        return now.data
    def min(self):
        now = self.root
        while now.left:
            now = now.left
        return now.data

    def find(self,key):
        return self._find(self.root,key)
    def _find(self,node,key):
        if node is None or node.data==key:
            return node is not None
        elif key<node.data:
            return self._find(node.left,key)
        else:
            return self._find(node.right,key)
    def delete(self,key):
        self.root,deleted=self._delete(self.root,key)
        return deleted
    def _delete(self,node,key):
        if node is None:
            return node,False
        deleted=False
        if key==node.data:
            deleted=True
            if node.left and node.right:
                parent,child=node,node.right
                while child.left is not None:
                    parent,child=child,child.left
                child.left=node.left
                if parent!=node:
                    parent.left=child.right
                    child.right=node.right
                node=child
            elif node.left or node.right:
                node=node.left or node.right
            else:
                node=None
        elif key<node.data:
            node.left,deleted=self._delete(node.left,key)
        else:
            node.right,deleted=self._delete(node.right,key)
        return node,deleted


class Album:
    def __init__(self , album_name):
        self.name = album_name
        self.parent = None
        self.children = {}
        self.children_names = BST()
        self.photos= set()
        self.photos_names = BST()

    def mkalb(self , album_name):
        if album_name in self.children:
            print("duplicated album name")
        else:
            new = Album(album_name)
            new.parent = self
            self.children[album_name] = new
            self.children_names.insert(album_name)
        return self

    def get_album_count(self):
        albums = len(self.children)
        for child in self.children.values():
            albums += child.get_album_count()
        return albums
    def get_photo_count(self):
        photos = len(self.photos)
        for child in self.children.values():
            photos += child.get_photo_count()
        return photos


    def rmalb(self, options):

        album_count= 0
        photos_count = 0

        if options == '-1':
            if self.children:
                album_count+=1

                target_name = self.children_names.min()
                target = self.children[target_name]
                album_count += target.get_album_count()
                photos_count += target.get_photo_count()
                self.children_names.delete(target_name)

                del self.children[target_name]
        elif options == '1':
            if self.children:
                album_count+=1
                target_name = self.children_names.max()
                target = self.children[target_name]
                album_count += target.get_album_count()
                photos_count += target.get_photo_count()
                self.children_names.delete(target_name)

                del self.children[target_name]
        elif options == '0':

            album_count += self.get_album_count()
            photos_count += self.get_photo_count() - len(self.photos)
            self.children_names = BST()
            self.children = {}
        else:
            if self.children_names.find(options):
                album_count += 1
                target = self.children[options]
                album_count += target.get_album_count()
                photos_count += target.get_photo_count()
                self.children_names.delete(options)
                del self.children[target.name]
        print(album_count, photos_count)
        return self

    def insert(self, photo_name):
        if photo_name in self.photos:
            print("duplicated photo name")
        else:
            self.photos_names.insert(photo_name)
            self.photos.add(photo_name)
        return self

    def delete(self, options):

        photo_count = 0
        if options == '-1':
            if self.photos:
                name = self.photos_names.min()
                self.photos_names.delete(name)
                self.photos.remove(name)
                photo_count +=1

        elif options == '0':
            photo_count += len(self.photos)
            self.photos_names=BST()
            self.photos = set()

        elif options == '1':
            if self.photos:
                name = self.photos_names.max()
                self.photos_names.delete(name)
                self.photos.remove(name)
                photo_count +=1

        else:
            if self.photos_names.find(options):
                self.photos_names.delete(options)
                self.photos.remove(options)
                photo_count +=1
        print(photo_count)
        return self

    def ca(self, options):

        if options == '..':
            if self.parent:
                print(self.parent.name)
                return self.parent
            else:
                print(self.name)
                return self
        elif options == '/':
            current = self
            while True:
                if current.parent:
                    current = current.parent
                else:
                    break
            print(current.name)
            return current
        else:
            if options in self.children:
                print(self.children[options].name)
                return self.children[options]
            else:
                print(self.name)
                return self
album = Album("album")
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    c, op = sys.stdin.readline().split()

    exec('album=album.' + c + "('"+ op +"')")
