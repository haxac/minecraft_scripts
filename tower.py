from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()
pos = mc.player.getTilePos()
mc.events.clearAll()

blockDictionary = {
	  0    :{"id":block.AIR.id,                           "dtag":0 }	#空気
	, 1    :{"id":block.STONE.id,                         "dtag":0 }	#石
	, 4    :{"id":block.COBBLESTONE.id,                   "dtag":0 }	#丸石
	, 44   :{"id":block.STONE_SLAB.id,                    "dtag":0 }	#石ハーフブロック
	, 44.5 :{"id":block.Block(block.STONE_SLAB.id, 5).id, "dtag":5 }	#石レンガハーフブロック
	, 44.58:{"id":block.Block(block.STONE_SLAB.id, 5).id, "dtag":13}	#石レンガハーフブロック 上向き
	, 50   :{"id":block.TORCH.id,                         "dtag":0 }	#松明
	, 5.0  :{"id":block.WOOD_PLANKS_OAK.id,               "dtag":0 }	#オークの木材
	, 5.1  :{"id":block.WOOD_PLANKS_SPRUCE.id,            "dtag":1 }	#マツの木材
	, 65   :{"id":block.LADDER.id,                        "dtag":4 }	#はしご +x方向
	, 65.5 :{"id":block.LADDER.id,                        "dtag":5 }	#はしご -x方向
	, 65.2 :{"id":block.LADDER.id,                        "dtag":2 }	#はしご +y方向
	, 65.3 :{"id":block.LADDER.id,                        "dtag":3 }	#はしご -y方向
	, 98   :{"id":block.STONE_BRICK.id,                   "dtag":0 }	#石レンガ
	, 109  :{"id":block.STONE_BRICK_STAIRS.id,            "dtag":0 }	#石レンガの階段 +x方向
	, 109.1:{"id":block.STONE_BRICK_STAIRS.id,            "dtag":1 }	#石レンガの階段 -x方向
	, 109.2:{"id":block.STONE_BRICK_STAIRS.id,            "dtag":2 }	#石レンガの階段 +y方向
	, 109.3:{"id":block.STONE_BRICK_STAIRS.id,            "dtag":3 }	#石レンガの階段 -y方向
	, 109.4:{"id":block.STONE_BRICK_STAIRS.id,            "dtag":4 }	#石レンガの階段 +x方向 上下逆
	, 109.5:{"id":block.STONE_BRICK_STAIRS.id,            "dtag":5 }	#石レンガの階段 -x方向 上下逆
	, 109.6:{"id":block.STONE_BRICK_STAIRS.id,            "dtag":6 }	#石レンガの階段 +y方向 上下逆
	, 109.7:{"id":block.STONE_BRICK_STAIRS.id,            "dtag":7 }	#石レンガの階段 -y方向 上下逆
	, 188  :{"id":block.SPRUCE_FENCE.id,                  "dtag":0 }	#マツのフェンス
}

b=[]

#1段目 基礎
a1=[]
a1.append([    0,    0,    0,   0,    0,   0,     0,      0,  0])  # +------->y
a1.append([    0,   98,   98,  98,   98,  98,    98,     98,  0])  # |
a1.append([    0,   98,   98,  98,   98,  98,    98,     98,  0])  # |
a1.append([109.2,   98,   98,  98,   98,  98,    98,     98,  0])  # |
a1.append([109.2,   98,   98,  98,   98,  98,    98,     98,  0])  # v
a1.append([109.2,   98,   98,  98,   98,  98,    98,     98,  0])  # x
a1.append([    0,   98,   98,  98,   98,  98,    98,     98,  0])  #
a1.append([    0,   98,   98,  98,   98,  98,    98,     98,  0])  #
a1.append([    0,    0,    0,   0,    0,   0,     0,      0,  0])  #
b.append(a1)
#2段目 床
a2=[]
a2.append([    0,    0,    0,   0,    0,   0,     0,      0])
a2.append([    0,    0,   98,   0, 44.5,   0,    98,      0])
a2.append([    0,   98,   98,   1,    1,   1,    98,     98])
a2.append([    0,    0,    1,  98,   98,  98,     1,      0])
a2.append([    0,    0,   98,  98,   98,  98,     1,   44.5])
a2.append([    0,    0,    1,  98,   98,  98,     1,      0])
a2.append([    0,   98,   98,   1,    1,   1,    98,     98])
a2.append([    0,    0,   98,   0, 44.5,   0,    98,      0])
b.append(a2)
#3段目
a3=[]
a3.append([    0,    0,    0,   0,    0,   0,     0,      0])
a3.append([    0,    0,   98,   0,    0,   0,    98,      0])
a3.append([    0,   98,   98,   1, 44.5,   1,    98,     98])
a3.append([    0,    0,   98,   0,    0,   0,     1,      0])
a3.append([    0,    0,    0,   0,    0,   0,  44.5,      0])
a3.append([    0,    0,   98,65.3,    0,   0,     1,      0])
a3.append([    0,   98,   98,   1, 44.5,   1,    98,     98])
a3.append([    0,    0,   98,   0,    0,   0,    98,      0])
b.append(a3)
#4段目
a4=[]
a4.append([    0,    0,    0,   0,    0,   0,      0,     0])
a4.append([    0,    0,   98,   0,    0,   0,     98,     0])
a4.append([    0,   98,   98,   1,44.58,   1,     98,    98])
a4.append([    0,    0,   98,   0,    0,   0,      1,     0])
a4.append([    0,    0,    0,   0,    0,   0,  44.58,     0])
a4.append([    0,    0,   98,65.3,    0,   0,      1,     0])
a4.append([    0,   98,   98,   1,44.58,   1,     98,    98])
a4.append([    0,    0,   98,   0,    0,   0,     98,     0])
b.append(a4)
#5段目
a5=[]
a5.append([    0,    0,    0,   0,    0,   0,      0,     0])
a5.append([    0,    0,   98,   0,    0,   0,     98,     0])
a5.append([    0,   98,   98,   1,    1,   1,     98,    98])
a5.append([    0,    0,   98,   0,    0,   0,      1,     0])
a5.append([    0,    0,    0,   0,    0,   0,      1,     0])
a5.append([    0,    0,   98,65.3,    0,   0,      1,     0])
a5.append([    0,   98,   98,   1,    1,   1,     98,    98])
a5.append([    0,    0,   98,   0,    0,   0,     98,     0])
b.append(a5)
#6段目
a6=[]
a6.append([    0,    0,    0,   0,    0,   0,      0,    0])
a6.append([    0,    0,   98,   0,    0,   0,     98,    0])
a6.append([    0,   98,   98,  98,   98,  98,     98,   98])
a6.append([    0,    0,   98, 5.1,  5.1, 5.1,     98,    0])
a6.append([    0,    0,   98, 5.1,  5.1, 5.1,     98,    0])
a6.append([    0,    0,   98,65.3,  5.1, 5.1,     98,    0])
a6.append([    0,   98,   98,  98,   98,  98,     98,   98])
a6.append([    0,    0,   98,   0,    0,   0,     98,    0])
b.append(a6)
#7段目
a7=[]
a7.append([    0,    0,    0,   0,    0,   0,      0,    0])
a7.append([    0,    0,   98,   0,    0,   0,     98,    0])
a7.append([    0,   98,   98,   1,    1,   1,     98,   98])
a7.append([    0,    0,    1,   0,    0,   0,      1,    0])
a7.append([    0,    0,    1,   0,    0,   0,      1,    0])
a7.append([    0,    0,    1,65.3,    0,   0,      1,    0])
a7.append([    0,   98,   98,   1,    1,   1,     98,   98])
a7.append([    0,    0,   98,   0,    0,   0,     98,    0])
b.append(a7)
#8段目
a8=[]
a8.append([    0,    0,    0,   0,    0,   0,      0,    0])
a8.append([    0,    0,  109,   0,    0,   0,    109,    0])
a8.append([    0,109.2,   98,   1, 44.5,   1,     98,109.3])
a8.append([    0,    0,    1,   0,    0,   0,      1,    0])
a8.append([    0,    0, 44.5,   0,    0,   0,   44.5,    0])
a8.append([    0,    0,    1,65.3,    0,   0,      1,    0])
a8.append([    0,109.2,   98,   1, 44.5,   1,     98,109.3])
a8.append([    0,    0,109.1,   0,    0,   0,  109.1,    0])
b.append(a8)
#9段目
a9=[]
a9.append([    0,    0,    0,   0,    0,   0,      0,    0])
a9.append([    0,    0,    0,   0,    0,   0,      0,    0])
a9.append([    0,    0,   98,   1,44.58,   1,     98,    0])
a9.append([    0,    0,    1,   0,    0,   0,      1,    0])
a9.append([    0,    0,44.58,   0,    0,   0,  44.58,    0])
a9.append([    0,    0,    1,65.3,    0,   0,      1,    0])
a9.append([    0,    0,   98,   1,44.58,   1,     98,    0])
a9.append([    0,    0,    0,   0,    0,   0,      0,    0])
b.append(a9)
#10段目
a10=[]
a10.append([   0,    0,    0,   0,    0,   0,      0,    0])
a10.append([   0,    0,    0,   0,    0,   0,      0,    0])
a10.append([   0,    0,   98,   1,    1,   1,     98,    0])
a10.append([   0,    0,    1,   0,    0,   0,      1,    0])
a10.append([   0,    0,    1,   0,    0,   0,      1,    0])
a10.append([   0,    0,    1,65.3,    0,   0,      1,    0])
a10.append([   0,    0,   98,   1,    1,   1,     98,    0])
a10.append([   0,    0,    0,   0,    0,   0,      0,    0])
b.append(a10)
#11段目
a11=[]
a11.append([   0,    0,    0,   0,    0,   0,      0,    0])
a11.append([   0,    0,    0,   0,    0,   0,      0,    0])
a11.append([   0,    0,   98,  98,   98,  98,     98,    0])
a11.append([   0,    0,   98,   0,    0,   0,     98,    0])
a11.append([   0,    0,   98,   0,    0,   0,     98,    0])
a11.append([   0,    0,   98,65.3,    0,   0,     98,    0])
a11.append([   0,    0,   98,  98,   98,  98,     98,    0])
a11.append([   0,    0,    0,   0,    0,   0,      0,    0])
b.append(a11)
#12段目
a12=[]
a12.append([   0,    0,    0,   0,    0,   0,      0,    0])
a12.append([   0,    0,    0,   0,    0,   0,      0,    0])
a12.append([   0,    0,   98,  98,   98,  98,     98,    0])
a12.append([   0,    0,   98,   0,    0,   0,     98,    0])
a12.append([   0,    0,   98,   0,    0,   0,     98,    0])
a12.append([   0,    0,   98,65.3,    0,   0,     98,    0])
a12.append([   0,    0,   98,  98,   98,  98,     98,    0])
a12.append([   0,    0,    0,   0,    0,   0,      0,    0])
b.append(a12)
#13段目
a13=[]
a13.append([   0,    0,    0,   0,    0,   0,      0,    0])
a13.append([   0,    0,   98, 188,   98, 188,     98,    0])
a13.append([   0,   98,   98,  98,   98,  98,     98,   98])
a13.append([   0,  188,   98, 5.1,  5.1, 5.1,     98,  188])
a13.append([   0,   98,   98, 5.1,  5.1, 5.1,     98,   98])
a13.append([   0,  188,   98,65.3,  5.1, 5.1,     98,  188])
a13.append([   0,   98,   98,  98,   98,  98,     98,   98])
a13.append([   0,    0,   98, 188,   98, 188,     98,    0])
b.append(a13)
#14段目
a14=[]
a14.append([   0,    0,    0,   0,    0,   0,      0,    0])
a14.append([   0,    0,   98,  98,   98,  98,     98,    0])
a14.append([   0,   98,    0,   0,    0,   0,      0,   98])
a14.append([   0,   98,    0,   0,    0,   0,      0,   98])
a14.append([   0,   98,    0,   0,    0,   0,      0,   98])
a14.append([   0,   98,    0,   0,    0,   0,      0,   98])
a14.append([   0,   98,    0,   0,    0,   0,      0,   98])
a14.append([   0,    0,   98,  98,   98,  98,     98,    0])
b.append(a14)
#15段目
a15=[]
a15.append([   0,    0,    0,   0,    0,   0,      0,    0])
a15.append([   0,    0, 44.5,  50, 44.5,  50,   44.5,    0])
a15.append([   0, 44.5,    0,   0,    0,   0,      0, 44.5])
a15.append([   0,   50,    0,   0,    0,   0,      0,   50])
a15.append([   0, 44.5,    0,   0,    0,   0,      0, 44.5])
a15.append([   0,   50,    0,   0,    0,   0,      0,   50])
a15.append([   0, 44.5,    0,   0,    0,   0,      0, 44.5])
a15.append([   0,    0, 44.5,  50, 44.5,  50,   44.5,    0])
b.append(a15)

#debug
#print(b)

'''
mc.setBlock(pos.x-2, pos.y, pos.z+1, block.STONE_BRICK_STAIRS.id, 0)
mc.setBlock(pos.x+0, pos.y, pos.z+1, block.STONE_BRICK_STAIRS.id, 1)
mc.setBlock(pos.x+2, pos.y, pos.z+1, block.STONE_BRICK_STAIRS.id, 2)
mc.setBlock(pos.x+4, pos.y, pos.z+1, block.STONE_BRICK_STAIRS.id, 3)
mc.setBlock(pos.x+6, pos.y, pos.z+1, block.STONE_BRICK_STAIRS.id, 4)
mc.setBlock(pos.x+8, pos.y, pos.z+1, block.STONE_BRICK_STAIRS.id, 5)
mc.setBlock(pos.x+10, pos.y, pos.z+1, block.STONE_BRICK_STAIRS.id, 6)
mc.setBlock(pos.x+12, pos.y, pos.z+1, block.STONE_BRICK_STAIRS.id, 7)
'''
#高さでループ
for height, l in enumerate(b):
	#面でループ
	for index, r in enumerate(b[height]):
		#行でループ
		for hoge, fuga in enumerate(b[height][index]):
			#print(fuga)
			mc.setBlock(pos.x+index, pos.y+height, pos.z+hoge, blockDictionary[fuga]["id"], blockDictionary[fuga]["dtag"])
