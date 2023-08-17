import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

@client.event
async def on_message(message):
    if message.channel.id == 1138311332333105292:
        # Rules
        if message.content.startswith('rules'):
            embedvar1 = discord.Embed(title="Selamat datang di Server Discord Rinju Group",
                                     description="Disini kita bisa saling ngobrol dan mabar bareng Rinju maupun Admin Rinju Comic."
                                                 "Disini kamu bebas mau bahas apa saja asalkan tetap sopan dan taat peraturan.\n"
                                                 "\n"
                                                 "Perlu diingat server ini boleh dimasuki oleh siapa saja. Dari simp/haters Rinju, yg kesepian mau nyari circle, nyari temen mabar, pokoknya semuanya. Boleh join."
            )
            embedvar1.add_field(name="\u200b", value="")
            embedvar1.add_field(name="PERATURAN CHAT", 
                                value=
                                "1. Dilarang bullying.\n"
                                "2. Dilarang berbuat SARA.\n"
                                "3. Dilarang berbuat rusuh atau tidak menyenangkan.\n"
                                "4. Dilarang spam chat dan gambar.\n"
                                "5. Boleh berkata kasar asal tidak menyakiti.\n"
                                "6. Boleh promosi tapi hanya di <#1120705960915243118>.\n" 
                                "7. Konten NSFW hanya di <#751735673194676244>, ambil kuncinya di <#936989198882336849>.\n", 
                                inline=False)
            embedvar1.add_field(name="PERATURAN MABAR", 
                                value=
                                "1. Selalu menghormati baik yang cupu maupun yang jago.\n"
                                "2. Boleh toxic dalam batas wajar.\n"
                                "3. Dilarang menggunakan cheat diam-diam.\n"
                                "4. Kondisikan mic agar tidak mengganggu.\n", 
                                inline=False)
            embedvar1.set_footer(text="Sewajarnya aja, jadi dewasa jangan dikit-dikit ngambek. Pake otaknya, sekiranya itu salah ya salah.")

            await message.channel.send("https://media.discordapp.net/attachments/751738777927417936/751811922801852467/Strip18.png?width=810&height=312")
            await message.channel.send(embed=embedvar1)
            await message.delete(delay=1)

        elif message.content.startswith('update_rules'):
            embedvar1_1 = discord.Embed(title="Selamat datang di Server Discord Rinju Group",
                                     description="Disini kita bisa saling ngobrol dan mabar bareng Rinju maupun Admin Rinju Comic."
                                                 "Disini kamu bebas mau bahas apa saja asalkan tetap sopan dan taat peraturan.\n"
                                                 "\n"
                                                 "Perlu diingat server ini boleh dimasuki oleh siapa saja. Dari simp/haters Rinju, yg kesepian mau nyari circle, nyari temen mabar, pokoknya semuanya. Boleh join.",
                                        color=0x2ecc71,
            )
            embedvar1_1.add_field(name="", value="\u200b")
            embedvar1_1.add_field(name="PERATURAN CHAT2", 
                                value=
                                "1. Dilarang bullying.\n"
                                "2. Dilarang berbuat SARA.\n"
                                "3. Dilarang berbuat rusuh atau tidak menyenangkan.\n"
                                "4. Dilarang spam chat dan gambar.\n"
                                "5. Boleh berkata kasar asal tidak menyakiti.\n"
                                "6. Boleh promosi tapi hanya di <#1120705960915243118>.\n" 
                                "7. Konten NSFW hanya di <#751735673194676244>, ambil kuncinya di <#936989198882336849>.\n", 
                                inline=False)
            embedvar1_1.add_field(name="PERATURAN MABAR", 
                                value=
                                "1. Selalu menghormati baik yang cupu maupun yang jago.\n"
                                "2. Boleh toxic dalam batas wajar.\n"
                                "3. Dilarang menggunakan cheat diam-diam.\n"
                                "4. Kondisikan mic agar tidak mengganggu.\n", 
                                inline=True)
            embedvar1_1.set_footer(text="Sewajarnya aja, jadi dewasa jangan dikit-dikit ngambek. Pake otaknya, sekiranya itu salah ya salah.")

            channel = client.get_channel(1138311332333105292)
            msg = await channel.fetch_message(1138338503420297248)
            await msg.edit(embed=embedvar1_1)
            await message.delete(delay=1)

        # Introduction
        if message.content.startswith('intro'):
            embedvar2 = discord.Embed(title="Introduction",
                                     description="Untuk dapat memasuki <#478542407043121175>, kamu harus isi intro di <#477900367112437762>"
                                     )
            embedvar2.add_field(name="\u200b", value="")
            embedvar2.add_field(name="FORMAT INTRODUCTION", 
                                value=
                                "\- \*Nama Asli:\n"
                                "\- Gender:\n"
                                "\- Umur:\n"
                                "\- Asal:\n"
                                "\- Tau server ini darimana:\n"
                                "\- Sebut satu nama temanmu yg sudah join server ini:\n" 
                                "\- \**Data lain: \n"
                                "\n"
                                "**\*WAJIB DIISI!.**\n"
                                "*Jika anda seorang Vtuber, bisa sekalian mencantumkan bukti yang sesuai.\n"
                                "**(Optional) Bisa diisi data lain seperti akun steam, game yg sedang dimainin, dll.\n",
                                inline=False)
            embedvar2.add_field(name="", value="\u200b")
            embedvar2.add_field(name="PENJELASAN", 
                                value=
                                "- Nama yg kamu cantumkan di <#477900367112437762> akan menentukan boleh tidaknya kamu untuk mendapatkan full akses di server discord ini.\n"
                                "- Nama itu akan digunakan sebagai nickname discord.\n"
                                "- Minimal cantumkan nama depan saja. Nama tengah/belakang optional.\n",
                                inline=False)
            embedvar2.add_field(name="", value="\u200b")
            embedvar2.add_field(name="SELANJUTNYA",
                                value=
                                "- Setelah mengisi<#477900367112437762> , tunggu sampai admin mereview intro kamu."
                                " Kalau kamu mengisi <#477900367112437762> dengan benar, kamu akan mendapatkan role untuk mendapatkan full akses."
                                " Tapi bila intro kamu diberi react <:no:492702953581576192>, admin menolak memberikan role dan harus mengisi intro lagi yg benar.\n"
                                "- Kalau kalian benar-benar yakin nama itu adalah nama kamu dan masih diberi react <:no:492702953581576192>."
                                "Kalian bisa komplen dengan DM <@380684183204528128> atau <@&572034275164160010>. Untuk fast respon DM ktp/tanda pengenal kamu."
                                " Tunjukan nama saja, sensor data lain.\n"
                                "- Bila ada member yg namanya sama (double name). Nama tengah/belakang/username discord akan digunakan sebagai nama belakang di server ini.\n"
                                "- Kamu bisa request ganti nama belakang discord bila merasa tidak nyaman dengan nama lengkap yg dijadikan nickname di server ini.\n", 
                                inline=False)
            embedvar2.set_footer(text="Kita akan bisa lebih dekat dengan saling memanggil nama")

            await message.channel.send("https://cdn.discordapp.com/attachments/733644155804188712/1138833355769659482/discord_intro_banner.jpg")
            await message.channel.send(embed=embedvar2)
            await message.delete(delay=1)

        elif message.content.startswith('update_intro'):
            embedvar2_1 = discord.Embed(title="Introduction2",
                                     description="Untuk dapat memasuki <#477911432709799936>, kamu harus isi intro di <#477900367112437762>",
                                     color=0x9b59b6,
                                     )
            embedvar2_1.add_field(name="\u200b", value="")
            embedvar2_1.add_field(name="FORMAT INTRODUCTION (langsung copas)", 
                                value=
                                "\- \*Nama Asli:\n"
                                "\- Gender:\n"
                                "\- Umur:\n"
                                "\- Asal:\n"
                                "\- Tau server ini darimana:\n"
                                "\- Sebut satu nama temanmu yg sudah join server ini:\n" 
                                "\- \**Data lain: \n"
                                "\n"
                                "**\*WAJIB DIISI!.**\n"
                                "*Jika anda seorang Vtuber, bisa sekalian mencantumkan bukti yang sesuai.\n"
                                "**(Optional) Bisa diisi data lain seperti akun steam, game yg sedang dimainin, dll.\n",
                                inline=False)
            embedvar2_1.add_field(name="", value="\u200b")
            embedvar2_1.add_field(name="PENJELASAN", 
                                value=
                                "- Nama yg kamu cantumkan di <#477900367112437762> akan menentukan boleh tidaknya kamu untuk mendapatkan full akses di server discord ini.\n"
                                "- Nama itu akan digunakan sebagai nickname discord.\n"
                                "- Minimal cantumkan nama depan saja. Nama tengah/belakang optional.\n",
                                inline=False)
            embedvar2_1.add_field(name="", value="\u200b")
            embedvar2_1.add_field(name="Contoh", 
                                value=
                                "\- \*Nama Asli: Asep\n"
                                "\- Gender: Laki\n"
                                "\- Umur: 69\n"
                                "\- Asal: Nganjuk\n"
                                "\- Tau server ini darimana: fesbuk\n"
                                "\- Sebut satu nama temanmu yg sudah join server ini: <@173724932398645249>\n" 
                                "\- \**Data lain: \n"
                                "\- steam:  https://steamcommunity.com/id/burjoawl/ \n",
                                inline=False)
            embedvar2_1.add_field(name="", value="\u200b")
            embedvar2_1.add_field(name="SELANJUTNYA",
                                value=
                                "- Setelah mengisi<#477900367112437762> , tunggu sampai admin mereview intro kamu."
                                " Kalau kamu mengisi <#477900367112437762> dengan benar, kamu akan mendapatkan role untuk mendapatkan full akses."
                                " Tapi bila intro kamu diberi react <:no:492702953581576192>, admin menolak memberikan role dan harus mengisi intro lagi yg benar.\n"
                                "- Kalau kalian benar-benar yakin nama itu adalah nama kamu dan masih diberi react <:no:492702953581576192>."
                                "Kalian bisa komplen dengan DM <@380684183204528128> atau <@&572034275164160010>. Untuk fast respon DM ktp/tanda pengenal kamu."
                                " Tunjukan nama saja, sensor data lain.\n"
                                "- Bila ada member yg namanya sama (double name). Nama tengah/belakang/username discord akan digunakan sebagai nama belakang di server ini.\n"
                                "- Kamu bisa request ganti nama belakang discord bila merasa tidak nyaman dengan nama lengkap yg dijadikan nickname di server ini.\n", 
                                inline=False)
            embedvar2_1.set_footer(text="Kita akan bisa lebih dekat dengan saling memanggil nama")

            channel = client.get_channel(1138311332333105292)
            msg = await channel.fetch_message(1138857798554366084)
            await msg.edit(embed=embedvar2_1)
            await message.delete(delay=1)

        # about
        if message.content.startswith('link'):
            embedvar3 = discord.Embed(title="Ikuti semuanya ya~",
                                      color=0xE74C3C,
                                     description=
                                    
                                    "Facebook Fanpage: \nhttps://www.facebook.com/rinjucomic/\n"
                                    "\n"
                                    "Instagram: \nhttps://www.instagram.com/rinjuliana\n"
                                    "\n"
                                    "X (Twitter): \nhttps://x.com/@rinjucomic\n"
                                    "\n"
                                    "Youtube Channel: \nhttps://www.youtube.com/c/rinjuchannel\n"
                                    "\n"
                                    "Trakteer: \nhttps://trakteer.id/rinju\n"
                                    "\n"
                                    "Discord Link Invite: \nhttps://discord.gg/rinju | https://discord.gg/WaNanYf\n"
                                    "\n"
                                    "Pixiv: \nhttps://www.pixiv.net/en/users/21807831/illustrations" 
                                     )
            embedvar3.set_thumbnail(url="https://scontent.fcgk18-1.fna.fbcdn.net/v/t39.30808-6/328951518_1245462736351869_1261450744254198511_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=be3454&_nc_eui2=AeGmGndYRT5fGEfNqahVa-L7Ks1SXvYA-GIqzVJe9gD4Yq88lmJa88L7S_Nl4nR4y-__LAnT5Uj3poBPx07Rss9d&_nc_ohc=GjKn5QD1jsUAX-5aE9_&_nc_ht=scontent.fcgk18-1.fna&oh=00_AfAWZUQvHPh879xLo7mg0rE2edmVXCIUTFa-O9ny-nEpUA&oe=64DB63AA")
            await message.channel.send("https://cdn.discordapp.com/attachments/733644155804188712/1139536166970990602/discord_link_banner.jpg")
            await message.channel.send(embed=embedvar3)
            await message.delete(delay=2)

        elif message.content.startswith('update_link'):
            embedvar3_1 = discord.Embed(title="Introduction2",
                                     description="Untuk dapat memasuki <#477911432709799936>, kamu harus isi intro di <#477900367112437762>",
                                     color=0x9b59b6,
                                     )
            embedvar3_1.add_field(name="\u200b", value="")
            embedvar3_1.add_field(name="FORMAT INTRODUCTION (langsung copas)", 
                                value=
                                "\- \*Nama Asli:\n"
                                "\- Gender:\n"
                                "\- Umur:\n"
                                "\- Asal:\n"
                                "\- Tau server ini darimana:\n"
                                "\- Sebut satu nama temanmu yg sudah join server ini:\n" 
                                "\- \**Data lain: \n"
                                "\n"
                                "**\*WAJIB DIISI!.**\n"
                                "*Jika anda seorang Vtuber, bisa sekalian mencantumkan bukti yang sesuai.\n"
                                "**(Optional) Bisa diisi data lain seperti akun steam, game yg sedang dimainin, dll.\n",
                                inline=False)
            embedvar3_1.add_field(name="", value="\u200b")
            embedvar3_1.add_field(name="PENJELASAN", 
                                value=
                                "- Nama yg kamu cantumkan di <#477900367112437762> akan menentukan boleh tidaknya kamu untuk mendapatkan full akses di server discord ini.\n"
                                "- Nama itu akan digunakan sebagai nickname discord.\n"
                                "- Minimal cantumkan nama depan saja. Nama tengah/belakang optional.\n",
                                inline=False)
            embedvar3_1.add_field(name="", value="\u200b")
            embedvar3_1.add_field(name="Contoh", 
                                value=
                                "\- \*Nama Asli: Asep\n"
                                "\- Gender: Laki\n"
                                "\- Umur: 69\n"
                                "\- Asal: Nganjuk\n"
                                "\- Tau server ini darimana: fesbuk\n"
                                "\- Sebut satu nama temanmu yg sudah join server ini: <@173724932398645249>\n" 
                                "\- \**Data lain: \n"
                                "\- steam:  https://steamcommunity.com/id/burjoawl/ \n",
                                inline=False)
            embedvar3_1.add_field(name="", value="\u200b")
            embedvar3_1.add_field(name="SELANJUTNYA",
                                value=
                                "- Setelah mengisi<#477900367112437762> , tunggu sampai admin mereview intro kamu."
                                " Kalau kamu mengisi <#477900367112437762> dengan benar, kamu akan mendapatkan role untuk mendapatkan full akses."
                                " Tapi bila intro kamu diberi react <:no:492702953581576192>, admin menolak memberikan role dan harus mengisi intro lagi yg benar.\n"
                                "- Kalau kalian benar-benar yakin nama itu adalah nama kamu dan masih diberi react <:no:492702953581576192>."
                                "Kalian bisa komplen dengan DM <@380684183204528128> atau <@&572034275164160010>. Untuk fast respon DM ktp/tanda pengenal kamu."
                                " Tunjukan nama saja, sensor data lain.\n"
                                "- Bila ada member yg namanya sama (double name). Nama tengah/belakang/username discord akan digunakan sebagai nama belakang di server ini.\n"
                                "- Kamu bisa request ganti nama belakang discord bila merasa tidak nyaman dengan nama lengkap yg dijadikan nickname di server ini.\n", 
                                inline=False)
            embedvar3_1.set_footer(text="Kita akan bisa lebih dekat dengan saling memanggil nama")

            channel = client.get_channel(1138311332333105292)
            msg = await channel.fetch_message(1138857798554366084)
            await msg.edit(embed=embedvar3_1)
            await message.delete(delay=1)
    else:
        return


client.run('token')