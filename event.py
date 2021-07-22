import discord
from discord.ext import commands
i=input()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Logged in As {0.user}".format(client))

def saytxt(path):
    with open(path,"r") as e:
        return e.read()
def addtxt(path,Str):
    with open(path,"r") as e:
        a=e.read()
    with open(path,"w") as e:
        e.write(str(a)+str(Str))
cashout_room_id=""
with open('data/cor',"r") as e:
    cashout_room_id=str(e.read())
@client.command()
@commands.has_permissions(administrator=True)
async def a(ctx,cmd=None,msg1=None,msg2=None,msg3=None,msg4=None):
    if cmd!=None:
        if cmd.lower()=="c" or cmd.lower()=="clear":
            if msg1!=None:
                try:
                    if msg1.lower()=="all":
                        await ctx.channel.purge()
                    else:
                        await ctx.channel.purge(limit=int(msg1)+1)
                except:
                    await ctx.channel.send("@"+ctx.author.name+' -Unsupported Integer')
            else:
                await ctx.channel.purge(limit=2)
        elif cmd.lower()=="h" or cmd.lower()=="help":
            await ctx.channel.purge(limit=1)
            await ctx.channel.send(saytxt('data/event/h menu'))
        elif cmd.lower()=="ech" or cmd.lower()=="eventcreatehelp":
            await ctx.channel.purge(limit=1)
            await ctx.channel.send(saytxt('data/event/e c h menu'))
        elif cmd.lower()=="ec" or cmd.lower()=="eventcreate":
            if msg1!=None:
                if msg1=="fott":
                    if msg2!=None:
                        if msg3!=None:
                            if msg4!=None:
                                addtxt('data/event/Event List',msg1+"%>#%"+msg3+"%>#%"+msg4+"\n")
                                await ctx.channel.purge(limit=1)
                                await ctx.channel.send(msg2)
                            else:
                                await ctx.channel.send('MSG4 is Empty')
                        else:
                            await ctx.channel.send('MSG3 is Empty')
                    else:
                        await ctx.channel.send('MSG2 is Empty')
                else:
                    await ctx.channel.send('Invalid MSG1 Type')
            else:
                await ctx.channel.send('MSG1 is Empty')
        elif cmd.lower()=="pay":
            if msg1!=None:
                if msg2!=None:
                    awr=""
                    found=False
                    nowhv=0
                    with open('data/user data/bank','r') as e:
                        for x in e.read().split("\n"):
                            if x.split("%>#%")[0].lower()==msg1.lower():
                                awr+=str(msg1+"%>#%"+str(int(x.split("%>#%")[1])+int(msg2)))+"\n"
                                found=True
                                nowhv=int(x.split("%>#%")[1])+int(msg2)
                            else:
                                awr+=x+"\n"
                    with open('data/user data/bank','w') as e:
                        e.write(awr)
                    if not found:
                        await ctx.channel.send("Couldn't Found "+msg1)
                    else:
                        await ctx.channel.send("`Successfully Send $"+msg2+" To The User With id-"+msg1+" Now The User Have $"+str(nowhv)+"`")
                else:
                    await ctx.channel.send('Invalid Amount To Pay')
            else:
                await ctx.channel.send("Invalid User")
        elif cmd.lower()=="cor":
            if msg1!=None:
                with open('data/cor','w') as e:
                    e.write(msg1)
                with open('data/cor',"r") as e:
                    global cashout_room_id
                    cashout_room_id=e.read()
                    await ctx.channel.send("`Successfully Set id-"+msg1+" As CashOut Room`")
            else:
                await ctx.channel.send("`MSG1 Is Empty. Put The Channel's Id There`")
        elif cmd.lower()=="cmsg":
            await ctx.channel.purge(limit=1)
            if msg1!=None:
                if msg2!=None:
                    channel=client.get_channel(int(msg1))
                    await channel.send(msg2)
                else:
                    await ctx.channel.send('`MSG2 Is Empty @'+ctx.author+"`")
            else:
                await ctx.channel.send('`MSG1 Is Empty @'+ctx.author+"`")
        elif cmd.lower()=="dm":
            await ctx.channel.purge(limit=1)
            if msg1!=None:
                if msg2!=None:
                    author=client.get_user(msg1)
                    await author.send(msg2)
                else:
                    await ctx.channel.send("@"+ctx.author+" Your MSG2 Is Empty")
            else:
                await ctx.channel.send("@" + ctx.author + " Your MSG1 Is Empty")
        else:
            await ctx.channel.send("@" + ctx.author.name + " -Couldn't Find Any Commands With Your CMD")
    else:
        await ctx.channel.send("@" + ctx.author.name + " -Your CMD Is Empty")
@client.command()
async def m(ctx,cmd,msg1=None):
    if cmd=="b" and msg1==None:
        found=False
        have=None
        with open('data/user data/bank','r') as e:
            for x in e.read().split("\n"):
                if x.split("%>#%")[0]==str(ctx.author.id):
                    have=int(x.split("%>#%")[1])
                    found=True
        if found:
            await ctx.channel.send("`" + ctx.author.name + " \nYou Have $"+str(have)+" In Your Bank\nYou Can Do !m bco (amount) < To Tell Our Admins That You Want To Cashout`")
        else:
            await ctx.channel.send("`"+ctx.author.name+"\nYou Don't Have an Bank Account\nGet Started By Typing !m bc To Create VBank Account`")
    elif cmd.lower()=="b" and msg1!=None or cmd.lower()=="bank" and msg1!=None:
        found = False
        have = None
        with open('data/user data/bank', 'r') as e:
            for x in e.read().split("\n"):
                if x.split("%>#%")[0] == msg1:
                    have = int(x.split("%>#%")[1])
                    found = True
        if found:
            await ctx.channel.send("`User With id-"+msg1+" Have $"+str(have)+"`")
        else:
            await ctx.channel.send("`Couldn't Find The User With id-"+msg1+"`")
    elif cmd.lower()=="h" or cmd.lower()=="help":
        await ctx.channel.send("`For @"+str(ctx.author)+"`\n"+saytxt("data/event/m h menu"))
    elif cmd.lower()=="bc" or cmd.lower()=="bankcreate":
        found = False
        with open('data/user data/bank', 'r') as e:
            for x in e.read().split("\n"):
                if x.split("%>#%")[0] == str(ctx.author.id):
                    found = True
        if found:
            await ctx.channel.send("`@"+str(ctx.author)+" There Is Already An Bank Account With Your id-"+str(ctx.author.id)+"`")
        else:
            addtxt("data/user data/bank",str(ctx.author.id)+"%>#%"+"0")
            await ctx.channel.send("`@"+str(ctx.author)+" Your Bank Account Were Successfully Created With Your id-"+str(ctx.author.id)+"`")
    elif cmd.lower()=="e":
        if msg1!=None:
            found=False
            won=False
            savethis=""
            with open("data/event/Event List","r") as e:
                for x in e.read().split("\n"):
                    if x.split("%>#%")[0]=="fott":
                        if x.split("%>#%")[1]==msg1:
                            found=True
                            won=x.split("%>#%")[2]
                        else:
                            await ctx.channel.send("`@"+str(ctx.author)+" Wrong Answer`")
                            savethis+=x+"\n"
                    else:
                        savethis+=x+"\n"
            with open("data/event/Event List","w") as e:
                e.write(savethis)
            if found and won!=False:
                await ctx.channel.send("`@"+str(ctx.author)+"! You Got It!\nThe Answer Was ("+msg1+")\nHere Is Your Prize "+won+"$`")
                addtxt('data/event/Event Winer GiveWay Left List',str(ctx.author.id)+" Has Won "+str(won)+"\n")
                awr = ""
                found = False
                with open('data/user data/bank', 'r') as e:
                    for x in e.read().split("\n"):
                        if x.split("%>#%")[0]==str(ctx.author.id):
                            awr += str(str(ctx.author.id) + "%>#%" + str(int(x.split("%>#%")[1])+int(won)))+"\n"
                            found = True
                        else:
                            awr += x + "\n"
                with open('data/user data/bank', 'w') as e:
                    e.write(awr)
                if not found:
                    addtxt("data/user data/bank",str(ctx.author.id)+"%>#%"+str(won)+"\n")
        else:
            await ctx.channel.send("`@"+str(ctx.author)+" Missing (ans)`")
    elif cmd=="bco" and msg1!=None and int(msg1)>0 or cmd=="bco" and msg1!=None and msg1=="all" :
        with open('data/cor',"r") as e:
            print(e.read())
            channel=client.get_channel(int(e.read()))
            await channel.send("@"+str(ctx.author.name)+" Wants To Cashout Amount "+msg1)
            await ctx.author.send("`Our Admins Will Get Your Message In 24 Hours Else Create An Ticket\nYou Can Also Do !m bco (amount) Again To Send The Message Again To Out Admins\nBut Dont Spawm Cuz You Might Get Banned`")
client.run(i)