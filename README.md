
# Eritrea: A Short Modern History - English / Amharic / Tigrinya videos

Outputs (Actions > Build history videos > Artifacts):
- history_en.mp4  (English, alternating male/female voice)
- history_am.mp4  (Amharic, alternating Ameha/Mekdes voices, 0.7 s pause after each sentence; set SENTENCE_PAUSE to change)
- history_ti.mp4  (Tigrinya: no free voice exists, so scenes are captioned over quiet music unless you add your own
  recordings as audio_ti/01.mp3 ... 15.mp3, one per scene; scene numbers match scenes_en.txt)
- history_<video>.<lang>.srt  subtitle files (en, am, ti) timed to each video - upload them in YouTube Studio > Subtitles.

Files: scenes_en.txt / scenes_am.txt / scenes_ti.txt (15 scenes each, same order). English header = Title | Date | map settings;
Amharic and Tigrinya headers = Title | Date (the map settings come from the English file).
Map settings: view=eritrea|horn ; style=ancient|coast|italian|british|federation|province|war|independent ; mark=Assab,Massawa,Asmara,Adwa,Aksum ; note=analysis
Maps use Natural Earth MODERN borders for orientation only (no historical border lines are drawn).

Upload: lang.py mapkit.py music.py scenes.py histmap.py make_history.py, the three scenes files, .github/workflows/history.yml.
Optional: music.mp3 (your own royalty-free piece) replaces the built-in synthesised music.

Amharic and Tigrinya texts, titles and map names are DRAFTS - have native speakers review them before publishing.
