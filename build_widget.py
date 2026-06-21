import os
import urllib.request

os.makedirs('app/src/main/java/com/gujrat/prayerwidget', exist_ok=True)
os.makedirs('app/src/main/res/xml', exist_ok=True)
os.makedirs('app/src/main/res/layout', exist_ok=True)
os.makedirs('app/src/main/res/values', exist_ok=True)
os.makedirs('app/src/main/res/font', exist_ok=True)
os.makedirs('gradle/wrapper', exist_ok=True)

# Download Jameel Noori Nastaleeq font
urllib.request.urlretrieve(
    'https://raw.githubusercontent.com/muhammadfaisal385/JameelNooriNastaleeqFont/master/JameelNooriNastaleeq.ttf',
    'app/src/main/res/font/jameel_noori.ttf'
)
print('Font downloaded!')

open('app/src/main/AndroidManifest.xml','w').write(
'<?xml version="1.0" encoding="utf-8"?>\n'
'<manifest xmlns:android="http://schemas.android.com/apk/res/android">\n'
'    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />\n'
'    <application android:allowBackup="true" android:label="Prayer Widget" android:theme="@android:style/Theme.DeviceDefault">\n'
'        <receiver android:name=".PrayerWidgetClassic" android:exported="true" android:label="Prayer Classic">\n'
'            <intent-filter><action android:name="android.appwidget.action.APPWIDGET_UPDATE" /></intent-filter>\n'
'            <meta-data android:name="android.appwidget.provider" android:resource="@xml/widget_info_classic" />\n'
'        </receiver>\n'
'        <receiver android:name=".PrayerWidgetGold" android:exported="true" android:label="Prayer Gold">\n'
'            <intent-filter><action android:name="android.appwidget.action.APPWIDGET_UPDATE" /></intent-filter>\n'
'            <meta-data android:name="android.appwidget.provider" android:resource="@xml/widget_info_gold" />\n'
'        </receiver>\n'
'        <receiver android:name=".PrayerWidgetSlate" android:exported="true" android:label="Prayer Slate">\n'
'            <intent-filter><action android:name="android.appwidget.action.APPWIDGET_UPDATE" /></intent-filter>\n'
'            <meta-data android:name="android.appwidget.provider" android:resource="@xml/widget_info_slate" />\n'
'        </receiver>\n'
'        <receiver android:name=".PrayerWidgetRose" android:exported="true" android:label="Prayer Rose">\n'
'            <intent-filter><action android:name="android.appwidget.action.APPWIDGET_UPDATE" /></intent-filter>\n'
'            <meta-data android:name="android.appwidget.provider" android:resource="@xml/widget_info_rose" />\n'
'        </receiver>\n'
'        <receiver android:name=".PrayerWidgetOcean" android:exported="true" android:label="Prayer Ocean">\n'
'            <intent-filter><action android:name="android.appwidget.action.APPWIDGET_UPDATE" /></intent-filter>\n'
'            <meta-data android:name="android.appwidget.provider" android:resource="@xml/widget_info_ocean" />\n'
'        </receiver>\n'
'        <service android:name=".CountdownService" android:exported="false" />\n'
'        <receiver android:name=".BootReceiver" android:exported="true">\n'
'            <intent-filter><action android:name="android.intent.action.BOOT_COMPLETED" /></intent-filter>\n'
'        </receiver>\n'
'    </application>\n'
'</manifest>\n')

for name in ['classic','gold','slate','rose','ocean']:
    open(f'app/src/main/res/xml/widget_info_{name}.xml','w').write(
    '<?xml version="1.0" encoding="utf-8"?>\n'
    '<appwidget-provider xmlns:android="http://schemas.android.com/apk/res/android"\n'
    '    android:minWidth="250dp" android:minHeight="110dp"\n'
    '    android:targetCellWidth="4" android:targetCellHeight="2"\n'
    '    android:updatePeriodMillis="1800000"\n'
    f'    android:initialLayout="@layout/widget_layout_{name}"\n'
    f'    android:previewLayout="@layout/widget_layout_{name}"\n'
    '    android:resizeMode="horizontal|vertical"\n'
    '    android:widgetCategory="home_screen">\n'
    '</appwidget-provider>\n')

def make_layout(accent):
    return (
    '<?xml version="1.0" encoding="utf-8"?>\n'
    '<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"\n'
    '    android:layout_width="match_parent" android:layout_height="match_parent"\n'
    '    android:orientation="vertical" android:padding="10dp">\n'
    '    <LinearLayout android:layout_width="match_parent" android:layout_height="0dp"\n'
    '        android:layout_weight="1" android:orientation="horizontal">\n'
    # Left side
    '        <LinearLayout android:layout_width="0dp" android:layout_height="match_parent"\n'
    '            android:layout_weight="1" android:orientation="vertical" android:gravity="center_vertical">\n'
    '            <TextView android:layout_width="wrap_content" android:layout_height="wrap_content"\n'
    '                android:text="NEXT PRAYER" android:textColor="#AAAAAA" android:textSize="9sp"/>\n'
    '            <TextView android:id="@+id/widget_prayer_name" android:layout_width="wrap_content"\n'
    '                android:layout_height="wrap_content" android:text="\u0639\u0635\u0631"\n'
    '                android:textColor="#FFFFFF" android:textSize="22sp" android:textStyle="bold"\n'
    '                android:fontFamily="@font/jameel_noori" android:textDirection="rtl"/>\n'
    '            <TextView android:id="@+id/widget_prayer_time" android:layout_width="wrap_content"\n'
    '                android:layout_height="wrap_content" android:text="--:-- --"\n'
    f'                android:textColor="{accent}" android:textSize="12sp"/>\n'
    '            <Chronometer android:id="@+id/widget_countdown"\n'
    '                android:layout_width="wrap_content" android:layout_height="wrap_content"\n'
    '                android:text="00:00:00" android:textColor="#FFFFFF"\n'
    '                android:textSize="26sp" android:textStyle="bold"\n'
    '                android:countDown="true"/>\n'
    '            <TextView android:id="@+id/widget_location" android:layout_width="wrap_content"\n'
    '                android:layout_height="wrap_content" android:text="Gujrat"\n'
    f'                android:textColor="{accent}" android:textSize="11sp" android:textStyle="bold"/>\n'
    '        </LinearLayout>\n'
    # Right side schedule
    '        <LinearLayout android:layout_width="155dp" android:layout_height="match_parent"\n'
    '            android:orientation="vertical" android:gravity="center_vertical">\n'
    '            <TextView android:layout_width="match_parent" android:layout_height="wrap_content"\n'
    '                android:text="TODAY SCHEDULE" android:textColor="#AAAAAA" android:textSize="8sp"\n'
    '                android:gravity="center" android:layout_marginBottom="4dp"/>\n'
    f'            <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="3dp"><TextView android:id="@+id/fajr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="\u0641\u062c\u0631" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold" android:fontFamily="@font/jameel_noori" android:textDirection="rtl"/><TextView android:id="@+id/fajr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="--:--" android:textColor="#88FFFFFF" android:textSize="13sp"/></LinearLayout>\n'
    f'            <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="3dp"><TextView android:id="@+id/dhuhr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="\u0638\u06c1\u0631" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold" android:fontFamily="@font/jameel_noori" android:textDirection="rtl"/><TextView android:id="@+id/dhuhr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="--:--" android:textColor="#88FFFFFF" android:textSize="13sp"/></LinearLayout>\n'
    f'            <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="3dp"><TextView android:id="@+id/asr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="\u0639\u0635\u0631" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold" android:fontFamily="@font/jameel_noori" android:textDirection="rtl"/><TextView android:id="@+id/asr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="--:--" android:textColor="#88FFFFFF" android:textSize="13sp"/></LinearLayout>\n'
    f'            <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="3dp"><TextView android:id="@+id/maghrib_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="\u0645\u063a\u0631\u0628" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold" android:fontFamily="@font/jameel_noori" android:textDirection="rtl"/><TextView android:id="@+id/maghrib_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="--:--" android:textColor="#88FFFFFF" android:textSize="13sp"/></LinearLayout>\n'
    f'            <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal"><TextView android:id="@+id/isha_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="\u0639\u0634\u0627\u0621" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold" android:fontFamily="@font/jameel_noori" android:textDirection="rtl"/><TextView android:id="@+id/isha_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="--:--" android:textColor="#88FFFFFF" android:textSize="13sp"/></LinearLayout>\n'
    '        </LinearLayout>\n'
    '    </LinearLayout>\n'
    # Bottom credit line
    '    <TextView android:layout_width="match_parent" android:layout_height="wrap_content"\n'
    f'        android:text="Prepared by Arslan Aslam Gujrat Police"\n'
    f'        android:textColor="{accent}" android:textSize="8sp" android:textStyle="bold"\n'
    '        android:gravity="center" android:layout_marginTop="3dp"/>\n'
    '</LinearLayout>\n')

open('app/src/main/res/layout/widget_layout_classic.xml','w').write(make_layout('#10B981'))
open('app/src/main/res/layout/widget_layout_gold.xml','w').write(make_layout('#F59E0B'))
open('app/src/main/res/layout/widget_layout_slate.xml','w').write(make_layout('#94A3B8'))
open('app/src/main/res/layout/widget_layout_rose.xml','w').write(make_layout('#FB7185'))
open('app/src/main/res/layout/widget_layout_ocean.xml','w').write(make_layout('#38BDF8'))

open('app/src/main/res/values/strings.xml','w').write(
'<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <string name="app_name">Prayer Widget</string>\n</resources>\n')

open('app/src/main/java/com/gujrat/prayerwidget/PrayerCalc.kt','w').write(
'package com.gujrat.prayerwidget\n'
'import android.os.SystemClock\n'
'import android.widget.RemoteViews\n'
'import java.util.Calendar\n'
'import kotlin.math.*\n'
'object PrayerCalc {\n'
'    private const val LAT = 32.5736\n'
'    private const val LNG = 74.0874\n'
'    private const val TZ = 5.0\n'
'    private val URDU_NAMES = mapOf("Fajr" to "\u0641\u062c\u0631", "Dhuhr" to "\u0638\u06c1\u0631", "Asr" to "\u0639\u0635\u0631", "Maghrib" to "\u0645\u063a\u0631\u0628", "Isha" to "\u0639\u0634\u0627\u0621")\n'
'    fun calcPrayerTimes(cal: Calendar): List<Triple<String,Int,String>> {\n'
'        val y=cal.get(Calendar.YEAR);val m=cal.get(Calendar.MONTH)+1;val d=cal.get(Calendar.DAY_OF_MONTH)\n'
'        val jd=367.0*y-(7*(y+(m+9)/12)/4)+(275*m/9)+d+1721013.5\n'
'        val D=jd-2451545.0\n'
'        val g=Math.toRadians(357.529+0.98560028*D)\n'
'        val L=280.459+0.98564736*D\n'
'        val lam=Math.toRadians(L+1.9148*sin(g)+0.02*sin(2*g))\n'
'        val ep=Math.toRadians(23.439-0.00000036*D)\n'
'        val RA=Math.toDegrees(atan2(cos(ep)*sin(lam),cos(lam)))/15.0\n'
'        val decl=Math.toDegrees(asin(sin(ep)*sin(lam)))\n'
'        val eqT=(L%360-0.0057183-RA*15)/15.0\n'
'        val noon=12.0+TZ-LNG/15.0-eqT\n'
'        fun ha(angle:Double):Double {\n'
'            val c=(sin(Math.toRadians(angle))-sin(Math.toRadians(LAT))*sin(Math.toRadians(decl)))/(cos(Math.toRadians(LAT))*cos(Math.toRadians(decl)))\n'
'            return Math.toDegrees(acos(c.coerceIn(-1.0,1.0)))/15.0\n'
'        }\n'
'        val fajr=noon-ha(-18.0)\n'
'        val dhuhr=noon\n'
'        val asrAlt=Math.toDegrees(atan(2.0+tan(Math.toRadians(abs(LAT-decl)))))\n'
'        val cAsr=(sin(Math.toRadians(90.0-asrAlt))-sin(Math.toRadians(LAT))*sin(Math.toRadians(decl)))/(cos(Math.toRadians(LAT))*cos(Math.toRadians(decl)))\n'
'        val asr=noon+Math.toDegrees(acos(cAsr.coerceIn(-1.0,1.0)))/15.0\n'
'        val maghrib=noon+ha(-0.833)\n'
'        val isha=noon+ha(-18.0)\n'
'        fun fmt(t:Double):Pair<Int,String> {\n'
'            val tt=((t%24)+24)%24;val h=tt.toInt();var min=((tt-h)*60).roundToInt()\n'
'            var hh=h;if(min>=60){min-=60;hh+=1}\n'
'            val ap=if(hh%24<12)"AM" else "PM";val h12=if(hh%12==0)12 else hh%12\n'
'            return Pair(hh*60+min,"$h12:${min.toString().padStart(2,\'0\')} $ap")\n'
'        }\n'
'        val(fm,fs)=fmt(fajr);val(dm,ds)=fmt(dhuhr);val(am,as2)=fmt(asr);val(mm,ms)=fmt(maghrib);val(im,is2)=fmt(isha)\n'
'        return listOf(Triple("Fajr",fm,fs),Triple("Dhuhr",dm,ds),Triple("Asr",am,as2),Triple("Maghrib",mm,ms),Triple("Isha",im,is2))\n'
'    }\n'
'    fun updateViews(views: RemoteViews, accentColor: Int) {\n'
'        val cal=Calendar.getInstance()\n'
'        val prayers=calcPrayerTimes(cal)\n'
'        val now=cal.get(Calendar.HOUR_OF_DAY)*60+cal.get(Calendar.MINUTE)\n'
'        val sec=cal.get(Calendar.SECOND)\n'
'        var next=prayers[0];var diff=Int.MAX_VALUE\n'
'        for(p in prayers){val d=p.second-now;if(d>0&&d<diff){diff=d;next=p}}\n'
'        if(diff==Int.MAX_VALUE){next=prayers[0];diff=1440-now+prayers[0].second}\n'
'        val totalSecs=(diff*60-sec).toLong()\n'
'        views.setChronometer(R.id.widget_countdown,SystemClock.elapsedRealtime()+totalSecs*1000L,"%02d:%02d:%02d",true)\n'
'        views.setTextViewText(R.id.widget_prayer_name, URDU_NAMES[next.first] ?: next.first)\n'
'        views.setTextViewText(R.id.widget_prayer_time,next.third)\n'
'        views.setTextViewText(R.id.widget_location,"Gujrat")\n'
'        views.setTextColor(R.id.widget_prayer_time,accentColor)\n'
'        views.setTextColor(R.id.widget_location,accentColor)\n'
'        val ids=listOf(Triple(R.id.fajr_name,R.id.fajr_time,prayers[0]),Triple(R.id.dhuhr_name,R.id.dhuhr_time,prayers[1]),Triple(R.id.asr_name,R.id.asr_time,prayers[2]),Triple(R.id.maghrib_name,R.id.maghrib_time,prayers[3]),Triple(R.id.isha_name,R.id.isha_time,prayers[4]))\n'
'        for((nId,tId,p) in ids){\n'
'            views.setTextColor(nId,if(p.first==next.first)accentColor else 0xCCFFFFFF.toInt())\n'
'            views.setTextColor(tId,if(p.first==next.first)accentColor else 0x88FFFFFF.toInt())\n'
'            views.setTextViewText(tId,p.third)\n'
'        }\n'
'    }\n'
'}\n')

for name, accent, layout in [
    ('Classic','0xFF10B981.toInt()','widget_layout_classic'),
    ('Gold','0xFFF59E0B.toInt()','widget_layout_gold'),
    ('Slate','0xFF94A3B8.toInt()','widget_layout_slate'),
    ('Rose','0xFFFB7185.toInt()','widget_layout_rose'),
    ('Ocean','0xFF38BDF8.toInt()','widget_layout_ocean')]:
    open(f'app/src/main/java/com/gujrat/prayerwidget/PrayerWidget{name}.kt','w').write(
    f'package com.gujrat.prayerwidget\n'
    'import android.appwidget.AppWidgetManager\nimport android.appwidget.AppWidgetProvider\n'
    'import android.content.Context\nimport android.content.Intent\nimport android.widget.RemoteViews\n'
    f'class PrayerWidget{name} : AppWidgetProvider() {{\n'
    '    override fun onUpdate(context: Context, appWidgetManager: AppWidgetManager, appWidgetIds: IntArray) {\n'
    '        for (id in appWidgetIds) {\n'
    f'            val views = RemoteViews(context.packageName, R.layout.{layout})\n'
    f'            PrayerCalc.updateViews(views, {accent})\n'
    '            appWidgetManager.updateAppWidget(id, views)\n'
    '        }\n'
    '        context.startService(Intent(context, CountdownService::class.java))\n'
    '    }\n'
    '    override fun onDisabled(context: Context) { context.stopService(Intent(context, CountdownService::class.java)) }\n'
    '}\n')

open('app/src/main/java/com/gujrat/prayerwidget/CountdownService.kt','w').write(
'package com.gujrat.prayerwidget\n'
'import android.app.Service\nimport android.appwidget.AppWidgetManager\n'
'import android.content.ComponentName\nimport android.content.Intent\n'
'import android.os.Handler\nimport android.os.IBinder\nimport android.os.Looper\nimport android.widget.RemoteViews\n'
'class CountdownService : Service() {\n'
'    private val handler = Handler(Looper.getMainLooper())\n'
'    private val runnable = object : Runnable {\n'
'        override fun run() {\n'
'            val mgr = AppWidgetManager.getInstance(this@CountdownService)\n'
'            val widgets = listOf(\n'
'                Triple(PrayerWidgetClassic::class.java, R.layout.widget_layout_classic, 0xFF10B981.toInt()),\n'
'                Triple(PrayerWidgetGold::class.java, R.layout.widget_layout_gold, 0xFFF59E0B.toInt()),\n'
'                Triple(PrayerWidgetSlate::class.java, R.layout.widget_layout_slate, 0xFF94A3B8.toInt()),\n'
'                Triple(PrayerWidgetRose::class.java, R.layout.widget_layout_rose, 0xFFFB7185.toInt()),\n'
'                Triple(PrayerWidgetOcean::class.java, R.layout.widget_layout_ocean, 0xFF38BDF8.toInt())\n'
'            )\n'
'            for ((cls, layout, accent) in widgets) {\n'
'                val ids = mgr.getAppWidgetIds(ComponentName(this@CountdownService, cls))\n'
'                for (id in ids) {\n'
'                    val v = RemoteViews(packageName, layout)\n'
'                    PrayerCalc.updateViews(v, accent)\n'
'                    mgr.updateAppWidget(id, v)\n'
'                }\n'
'            }\n'
'            handler.postDelayed(this, 1000)\n'
'        }\n'
'    }\n'
'    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int { handler.post(runnable); return START_STICKY }\n'
'    override fun onDestroy() { handler.removeCallbacks(runnable); super.onDestroy() }\n'
'    override fun onBind(intent: Intent?): IBinder? = null\n'
'}\n')

open('app/src/main/java/com/gujrat/prayerwidget/BootReceiver.kt','w').write(
'package com.gujrat.prayerwidget\n'
'import android.content.BroadcastReceiver\nimport android.content.Context\nimport android.content.Intent\n'
'class BootReceiver : BroadcastReceiver() {\n'
'    override fun onReceive(context: Context, intent: Intent) {\n'
'        if (intent.action == Intent.ACTION_BOOT_COMPLETED)\n'
'            context.startService(Intent(context, CountdownService::class.java))\n'
'    }\n'
'}\n')

open('gradle.properties','w').write('android.useAndroidX=true\nandroid.enableJetifier=true\n')
open('build.gradle','w').write('plugins {\n id "com.android.application" version "8.3.0" apply false\n id "org.jetbrains.kotlin.android" version "1.9.0" apply false\n}\n')
open('app/build.gradle','w').write('plugins {\n id "com.android.application"\n id "org.jetbrains.kotlin.android"\n}\nandroid {\n namespace "com.gujrat.prayerwidget"\n compileSdk 34\n defaultConfig {\n applicationId "com.gujrat.prayerwidget"\n minSdk 26\n targetSdk 34\n versionCode 1\n versionName "1.0"\n }\n compileOptions {\n sourceCompatibility JavaVersion.VERSION_17\n targetCompatibility JavaVersion.VERSION_17\n }\n kotlinOptions { jvmTarget = "17" }\n}\ndependencies {\n implementation "androidx.core:core-ktx:1.12.0"\n implementation "androidx.appcompat:appcompat:1.6.1"\n}\n')
open('settings.gradle','w').write('pluginManagement {\n repositories { google(); mavenCentral(); gradlePluginPortal() }\n}\ndependencyResolutionManagement {\n repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)\n repositories { google(); mavenCentral() }\n}\nrootProject.name = "PrayerWidget"\ninclude ":app"\n')
open('gradle/wrapper/gradle-wrapper.properties','w').write('distributionBase=GRADLE_USER_HOME\ndistributionPath=wrapper/dists\ndistributionUrl=https\\://services.gradle.org/distributions/gradle-8.4-bin.zip\nzipStoreBase=GRADLE_USER_HOME\nzipStorePath=wrapper/dists\n')

urllib.request.urlretrieve('https://raw.githubusercontent.com/gradle/gradle/v8.4.0/gradlew','gradlew')
os.chmod('gradlew',0o755)
print('Done! Urdu font + credit line added!')
