# Declaring node class to create objects and nodes
class Node:
  def __init__(self, name=None,val=None):
    self.name=name
    self.song=val
    self.next=None
    self.prev=None
#Declaring Linked list with variables and its function i.e Insert, jump(toNode), display, next,prev,play (to return head of the list)
class DoubleLL:
  def __init__(self,name=None):
    self.head=None
    self.playlist=name
  def Display(self):
    if self.head is None:
      print("\t\t\t\t\t\t\t\t\t\t\tList is empty")
      return
    else:
      n=self.head
      print("\t\t\t\t\t\t\t\t\t\tSongs List:-")
      i=1
      while n is not None:
        print(f"\t\t\t\t\t\t\t\t\t\t\t{i}){n.name}")
        n=n.next
        i+=1
  def Insert(self,name,val):
    if self.head is None:
      self.head=Node(name,val)
    else:
      n=self.head
      while n.next is not None:
        n=n.next
      new=Node(name,val)
      new.prev=n
      n.next=new
  def NextNode(self,node):
      if(node.next==None):
         return None
      else: node=node.next
      return node
  def PrevNode(self,node):
      node=node.prev
      return node
  def ToSong(self,num):
    if self.head is None:
      print("\t\t\t\t\t\t\t\t\t\t\tList is empty")
    else:
      n=self.head
      num-=1
      while n.next is not None and (num!=0):
        n=n.next
        num-=1
      return n
  def PlaySong(self):
    if self.head is None:
      print("\t\t\t\t\t\t\t\t\t\t\tSongs list is empty")
    else:
      n=self.head
      return n
#declaring predefined list named All Songs
lists=DoubleLL("All Songs")
lists.head= Node("One Love","onelove.mp3")
ex=Node("Ashes","ashes.mp3")
ex2=Node("Stranger","stranger.mp3")
lists.head.next=ex
ex.prev=lists.head
ex.next=ex2
ex2.prev=ex
lists.Insert("Haiwaan","haiwaan.mp3")
lists.Insert("Raule","Raule.mp3")
lists.Insert("Goliyan","Goliyan.mp3")
lists.Insert("El Dorado","El Dorado.mp3")
lists.Insert("Udta Punjab","Udta Punjab.mp3")

l1=Node("Haiwaan","haiwaan.mp3")
punjabi=DoubleLL("Punjabi Songs")
punjabi.head=l1
l2=Node("Raule","Raule.mp3")
l3=Node("Goliyan","Goliyan.mp3")
l4=Node("Udta Punjab","Udta Punjab.mp3")
l1.next=l2
l2.prev=l1
l2.next=l3
l3.next=l4
l3.prev=l2
l4.prev=l3
playlists=[]
playlists.append(lists)
playlists.append(punjabi)
## Creating new plalists 
def Playlists():
   flag=0
   new_lists=input("\t\t\t\t\t\t\t\t\t\tEnter name of the new playlist:- ")
   for i in playlists:
      if(i.playlist==new_lists):
         print("\t\t\t\t\t\t\t\t\t\t-----Playlists Already exist-----")
         flag=1
         break
   if(flag==0):
    x=DoubleLL(new_lists)
    playlists.append(x)
    return x
   else: return None

#Displaying playlists
def ShowPlaylists():
   print("\t\t\t\t\t\t\t\t\t\t***************************************")
   count=1
   for i in playlists:
      print(f"\t\t\t\t\t\t\t\t\t\t\t{count}) {i.playlist}")
      count+=1
# lists.Display()
# print()
# lists.Display()
# print()
## Importing necessary libraries to play songs 
import pygame
pygame.init()
from pygame import mixer
pygame.mixer.init()
## declaring play section of song with and without index(from first song of playlist)
def PlayMusic(pl,index):
  play=0
  if(index==None):
    x=pl.head
    while(True):
                print("\t\t\t\t\t\t\t\t\t\t***************************************")
                y=int(input("\t\t\t\t\t\t\t\t\t\t\t1)Next  \n\t\t\t\t\t\t\t\t\t\t\t2)Prev  \n\t\t\t\t\t\t\t\t\t\t\t3)Set Volume \n\t\t\t\t\t\t\t\t\t\t\t4)Pause/Play \n\t\t\t\t\t\t\t\t\t\t\t5)Stop\n\t\t\t\t\t\t\t\t\t\tEnter your choice:- "))
                print("\t\t\t\t\t\t\t\t\t\t***************************************")                
                if(y==1):
                    x=pl.NextNode(x)
                    if(x==None):
                        print("\t\t\t\t\t\t\t\t\t\t-----No more songs available-----")
                        print()
                        break
                    else: 
                        print("\t\t\t\t\t\t\t\t\t\t\t",x.name)
                        Play(x)
                elif y==2:
                    x=lists.PrevNode(x)
                    if(x==None):
                        print("\t\t\t\t\t\t\t\t\t\t-----No more songs available-----")
                        print()
                        break
                    else: 
                       print("\t\t\t\t\t\t\t\t\t\t\t",x.name)
                       Play(x)
                elif y==3:
                 pygame.mixer.music.set_volume(int(input("\t\t\t\t\t\t\t\t\t\tEnter volume in range of 1-10: "))/10)
                elif y==4:
                  if(play==0):
                    pygame.mixer.music.pause()
                    play=1
                  else:
                    pygame.mixer.music.unpause()
                    play=0
                else:
                    mixer.music.stop()
                    break
  else:
     x=pl.ToSong(index)
     Play(x)
     while(True):
                print("\t\t\t\t\t\t\t\t\t\t***************************************")
                y=int(input("\t\t\t\t\t\t\t\t\t\t\t1)Next  \n\t\t\t\t\t\t\t\t\t\t\t2)Prev  \n\t\t\t\t\t\t\t\t\t\t\t3)Set Volume \n\t\t\t\t\t\t\t\t\t\t\t4)Pause/Play \n\t\t\t\t\t\t\t\t\t\t\t5)Stop\n\t\t\t\t\t\t\t\t\t\tEnter your choice:- "))
                print("\t\t\t\t\t\t\t\t\t\t***************************************")                
                if(y==1):
                    x=pl.NextNode(x)
                    if(x==None):
                        print("\t\t\t\t\t\t\t\t\t\t-----No more songs available-----")
                        print()
                        break
                    else: 
                       print("\t\t\t\t\t\t\t\t\t\t\t",x.name)
                       Play(x)
                elif y==2:
                    x=pl.PrevNode(x)
                    if(x==None):
                        print("\t\t\t\t\t\t\t\t\t\t-----No more songs available-----")
                        print()
                        break
                    else: 
                       print("\t\t\t\t\t\t\t\t\t\t\t",x.name)
                       Play(x)
                elif y==3:
                 pygame.mixer.music.set_volume(int(input("\t\t\t\t\t\t\t\t\t\tEnter volume in range of 1-10: "))/10)
                elif y==4:
                  if(play==0):
                    pygame.mixer.music.pause()
                    play=1
                  else:
                    pygame.mixer.music.unpause()
                    play=0
                else:
                    mixer.music.stop()
                    break
## functiion to play song
def Play(Node):
  mixer.music.load(Node.song)
  mixer.music.play()

## Function For Playing and other options within the playlists
def Playing(x):
    while True:
        print("\t\t\t\t\t\t\t\t\t\t***************************************")
        i=int(input("\t\t\t\t\t\t\t\t\t\t\t1)Play Music\n\t\t\t\t\t\t\t\t\t\t\t2)Display Songs list\n\t\t\t\t\t\t\t\t\t\t\t3)Play Specific Song\n\t\t\t\t\t\t\t\t\t\t\t4)Add Song\n\t\t\t\t\t\t\t\t\t\t\t5)Go Back\n\t\t\t\t\t\t\t\t\t\tEnter your choice:-"))
        if(i==1):
            z=x.PlaySong()
            print("\t\t\t\t\t\t\t\t\t\t\t",z.name)
            Play(z)
            PlayMusic(x,None)
        elif(i==2):
            x.Display()
        elif(i==3):
            x.Display()
            index = int(input("\t\t\t\t\t\t\t\t\t\tEnter the Song Index:-"))
            PlayMusic(x,index)
        elif(i==4):
            name=input("\t\t\t\t\t\t\t\t\t\tEnter Song Name:-")
            song=input("\t\t\t\t\t\t\t\t\t\tEnter Song with extension:-")
            if(name=="" or song==""):
              print("\t\t\t\t\t\t\t\t\t\t-----Enter valid name and format-----")
            else:
              flag=0
              ptr=x.head
              ptr=playlists[0].head
              while ptr is not None:
                if(ptr.name==name):
                  flag=1
                  break
                else:
                  ptr=ptr.next
              if(flag==0):
                x.Insert(name,song)
              if(x!=playlists[0]):
                  flag=0
                  ptr=playlists[0].head
                  while ptr is not None:
                      if(ptr.name==name):
                          flag=1
                          break
                      else:
                          ptr=ptr.next
                  if(flag==0):
                      playlists[0].Insert(name,song)
                  else: print("\t\t\t\t\t\t\t\t\t\t\tSong already present in the AllSong list")   
        else:
            break
    

### Stsrt of program with selecting the playlist
while True:
  print("\t\t\t\t\t\t\t\t\t\t\t1) Select Playlists  \n\t\t\t\t\t\t\t\t\t\t\t2) Create New Playlist  \n\t\t\t\t\t\t\t\t\t\t\t3) End")
  select= int(input("\t\t\t\t\t\t\t\t\t\tEnter your choice:- "))
  if(select==1):
     ShowPlaylists()
     sel=int(input("\t\t\t\t\t\t\t\t\t\tSelect the playlist: "))
     if(sel>len(playlists)):
        print("\t\t\t\t\t\t\t\t\t\t\tEnter valid list index")
     else:
      z=playlists[sel-1]
      Playing(z)
  elif(select==2):
     x=Playlists()
     if(x!=None):
      name=input("\t\t\t\t\t\t\t\t\t\tEnter Song Name:-")
      song=input("\t\t\t\t\t\t\t\t\t\tEnter Song with extension:-")
      print(name)
      if(name=="" or song==""):  ## to check if input is not empty
         print("\t\t\t\t\t\t\t\t\t\t-----Enter valid name and format-----")
      else:
        x.Insert(name,song)
        playlists[0].Insert(name,song)            
        Playing(x)
  else:
    break