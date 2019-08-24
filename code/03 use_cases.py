# Build a game for random selection
# ---------------------------------
def get_track_and_voice():
    import random
    song_list = ["Closer", "Despacito", "Shape of You", "Love Yourself", "Girls like you", "Havana"]
    voice_list = ["Udit Narayan", "Sonu Nigam", "Shaan", "Shreya Ghoshal", "Yo Yo Honey Singh", "Badshah"]
    select_song = random.choice(song_list)
    select_voice = random.choice(voice_list)
    return(select_song, select_voice)


# Build a lambda / function for rolling a dice
# --------------------------------------------
def get_dice_roll_val(number_of_dice=1)
    import random
    min = 1
    max = 6
    total_roll_value = 0
    for i in range(0, number_of_dice):
        total_roll_value += random.randint(min, max)
    return total_roll_value


# Upload data to a local / hosted Database
# and query from a AWS / Azure endpoint
# -------------------------------------------
def get_list_from_db(count):
    import MySQLdb
    db = MySQLdb.connect(host="183.83.170.228:8090", #localhost
                        #user="demouser",
                        #passwd="demopass@123",
                        db="garmindb")

    cur = db.cursor()
    cur.execute("SELECT top(@%s) * FROM garmindb.Locations")

    locs = []
    for row in cur.fetchall():
        locs.append(row)
    
    db.close()
    return ",".join(locs)

# Event processing using kafka
# -----------------------------
def get_kafka_data():
    from kafka import KafkaConsumer
    # To consume latest messages and auto-commit offsets
    consumer = KafkaConsumer('my-topic',
                            group_id='my-group',
                            bootstrap_servers=['localhost:9092'])
    values = []
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        values.append(message.value)


# Similar APIs for graphQL and Redis