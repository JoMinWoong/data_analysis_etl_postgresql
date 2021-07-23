# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE public.songplays
(
    songplay_id serial,
    song_id character varying COLLATE pg_catalog."default",
    user_id character varying COLLATE pg_catalog."default",
    level character varying COLLATE pg_catalog."default",
    start_time character varying COLLATE pg_catalog."default",
    artist_id character varying COLLATE pg_catalog."default",
    session_id character varying COLLATE pg_catalog."default",
    location character varying COLLATE pg_catalog."default",
    user_agent character varying COLLATE pg_catalog."default",
    CONSTRAINT songplays_pkey PRIMARY KEY (songplay_id),
    CONSTRAINT fk_artist_id FOREIGN KEY (artist_id)
        REFERENCES public.artist (artist_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_song_id FOREIGN KEY (song_id)
        REFERENCES public.songs (song_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_start_time FOREIGN KEY (start_time)
        REFERENCES public.times (start_time) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id)
        REFERENCES public.users (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
""")

user_table_create = ("""
CREATE TABLE public.users
(
    user_id character varying COLLATE pg_catalog."default" NOT NULL,
    first_name character varying COLLATE pg_catalog."default",
    last_name character varying COLLATE pg_catalog."default",
    gender character varying COLLATE pg_catalog."default",
    level character varying COLLATE pg_catalog."default",
    CONSTRAINT users_pkey PRIMARY KEY (user_id)
);
""")

song_table_create = ("""
CREATE TABLE public.songs
(
    song_id character varying COLLATE pg_catalog."default" NOT NULL,
    title character varying COLLATE pg_catalog."default",
    artist_id character varying COLLATE pg_catalog."default",
    year smallint,
    duration double precision,
    CONSTRAINT songs_pkey PRIMARY KEY (song_id)
);
""")

artist_table_create = ("""
CREATE TABLE public.artist
(
    artist_id character varying COLLATE pg_catalog."default" NOT NULL,
    name character varying COLLATE pg_catalog."default",
    location character varying COLLATE pg_catalog."default",
    latitude double precision,
    longitude double precision,
    CONSTRAINT artist_pkey PRIMARY KEY (artist_id)
);
""")

time_table_create = ("""
CREATE TABLE public.times
(
    start_time character varying COLLATE pg_catalog."default" NOT NULL,
    hour smallint,
    day smallint,
    week smallint,
    month smallint,
    year smallint,
    weekday smallint,
    CONSTRAINT times_pkey PRIMARY KEY (start_time)
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO public.songplays(
song_id, user_id, level, start_time, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO public.users(user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO public.songs(song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO public.artist(artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO public.times(start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id from songs AS s LEFT OUTER JOIN artist as a ON s.artist_id = a.artist_id WHERE s.title = %s AND a.name = %s AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]