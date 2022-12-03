<video width="320" height="240" controls>
    <source src="1minEMDR.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>


vidPath = '1minEMDR.mp4'
window= pyglet.window.Window()
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)

player.queue(MediaLoad)
player.play()


@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(50,50)


pyglet.app.run()


# --- EMDR ----

if st.button('60 seconds EMDR'):
    video_file = open('1minEMDR.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
if st.button('30 seconds EMDR'):
    st.write('Goodbye')
if st.button('90 seconds EMDR'):
    st.write('Goodbye')
else: 
    st.write('Goodbye')
#button

# ---- openingszinnen ----

st.write('\n')
st.subheader("Welkomstbericht")
st.write("Welkom allen! Hierbij een moderne uitgave van een CV."
" En voor mij een leuk leerproject!"
" Hopelijk vind je het een leuk voorproefje voor wat ik voor jouw organizatie kan betekenen!"
)