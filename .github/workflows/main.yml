import os
import urllib.request

os.makedirs('app/src/main/java/com/gujrat/prayerwidget', exist_ok=True)
os.makedirs('app/src/main/res/xml', exist_ok=True)
os.makedirs('app/src/main/res/layout', exist_ok=True)
os.makedirs('app/src/main/res/values', exist_ok=True)
os.makedirs('gradle/wrapper', exist_ok=True)

open('app/src/main/AndroidManifest.xml','w').write('<?xml version="1.0" encoding="utf-8"?>\n<manifest xmlns:android="http://schemas.android.com/apk/res/android">\n    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />\n    <application android:allowBackup="true" android:label="Prayer Widget" android:theme="@android:style/Theme.DeviceDefault">\n        <receiver android:name=".PrayerWidgetProvider" android:exported="true">\n            <intent-filter><action android:name="android.appwidget.action.APPWIDGET_UPDATE" /></intent-filter>\n            <meta-data android:name="android.appwidget.provider" android:resource="@xml/prayer_widget_info" />\n        </receiver>\n        <service android:name=".PrayerUpdateService" android:exported="false" />\n        <receiver android:name=".BootReceiver" android:exported="true">\n            <intent-filter><action android:name="android.intent.action.BOOT_COMPLETED" /></intent-filter>\n        </receiver>\n    </application>\n</manifest>\n')

open('app/src/main/res/xml/prayer_widget_info.xml','w').write('<?xml version="1.0" encoding="utf-8"?>\n<appwidget-provider xmlns:android="http://schemas.android.com/apk/res/android"\n    android:minWidth="250dp"\n    android:minHeight="110dp"\n    android:targetCellWidth="4"\n    android:targetCellHeight="2"\n    android:updatePeriodMillis="1800000"\n    android:initialLayout="@layout/prayer_widget_layout"\n    android:previewLayout="@layout/prayer_widget_layout"\n    android:resizeMode="horizontal|vertical"\n    android:widgetCategory="home_screen">\n</appwidget-provider>\n')

open('app/src/main/res/layout/prayer_widget_layout.xml','w').write(
'<?xml version="1.0" encoding="utf-8"?>\n'
'<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"\n'
'    android:layout_width="match_parent" android:layout_height="match_parent"\n'
'    android:orientation="horizontal" android:padding="12dp">\n'
'    <LinearLayout android:layout_width="0dp" android:layout_height="match_parent"\n'
'        android:layout_weight="1" android:orientation="vertical" android:gravity="center_vertical">\n'
'        <TextView android:layout_width="wrap_content" android:layout_height="wrap_content"\n'
'            android:text="NEXT PRAYER" android:textColor="#7AADA0" android:textSize="9sp"/>\n'
'        <TextView android:id="@+id/widget_prayer_name" android:layout_width="wrap_content"\n'
'            android:layout_height="wrap_content" android:text="Asr"\n'
'            android:textColor="#FFFFFF" android:textSize="22sp" android:textStyle="bold"/>\n'
'        <TextView android:id="@+id/widget_prayer_time" android:layout_width="wrap_content"\n'
'            android:layout_height="wrap_content" android:text="5:03 PM"\n'
'            android:textColor="#10B981" android:textSize="12sp"/>\n'
'        <TextView android:id="@+id/widget_countdown" android:layout_width="wrap_content"\n'
'            android:layout_height="wrap_content" android:text="01:49:52"\n'
'            android:textColor="#FFFFFF" android:textSize="26sp" android:textStyle="bold"/>\n'
'        <TextView android:id="@+id/widget_location" android:layout_width="wrap_content"\n'
'            android:layout_height="wrap_content" android:text="Gujrat"\n'
'            android:textColor="#10B981" android:textSize="11sp" android:textStyle="bold"/>\n'
'    </LinearLayout>\n'
'    <LinearLayout android:layout_width="145dp" android:layout_height="match_parent"\n'
'        android:orientation="vertical" android:gravity="center_vertical">\n'
'        <TextView android:layout_width="match_parent" android:layout_height="wrap_content"\n'
'            android:text="TODAY SCHEDULE" android:textColor="#7AADA0" android:textSize="8sp"\n'
'            android:gravity="center" android:layout_marginBottom="4dp"/>\n'
'        <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="3dp"><TextView android:id="@+id/fajr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Fajr" android:textColor="#CCFFFFFF" android:textSize="10sp" android:textStyle="bold"/><TextView android:id="@+id/fajr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="3:15 AM" android:textColor="#88FFFFFF" android:textSize="10sp"/></LinearLayout>\n'
'        <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="3dp"><TextView android:id="@+id/dhuhr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Dhuhr" android:textColor="#CCFFFFFF" android:textSize="10sp" android:textStyle="bold"/><TextView android:id="@+id/dhuhr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="12:05 PM" android:textColor="#88FFFFFF" android:textSize="10sp"/></LinearLayout>\n'
'        <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="3dp"><TextView android:id="@+id/asr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Asr" android:textColor="#CCFFFFFF" android:textSize="10sp" android:textStyle="bold"/><TextView android:id="@+id/asr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="5:03 PM" android:textColor="#88FFFFFF" android:textSize="10sp"/></LinearLayout>\n'
'        <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="3dp"><TextView android:id="@+id/maghrib_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Maghrib" android:textColor="#CCFFFFFF" android:textSize="10sp" android:textStyle="bold"/><TextView android:id="@+id/maghrib_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="7:14 PM" android:textColor="#88FFFFFF" android:textSize="10sp"/></LinearLayout>\n'
'        <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal"><TextView android:id="@+id/isha_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Isha" android:textColor="#CCFFFFFF" android:textSize="10sp" android:textStyle="bold"/><TextView android:id="@+id/isha_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="8:55 PM" android:textColor="#88FFFFFF" android:textSize="10sp"/></LinearLayout>\n'
'    </LinearLayout>\n'
'</LinearLayout>\n')

open('app/src/main/res/values/strings.xml','w').write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <string name="app_name">Prayer Widget</string>\n</resources>\n')

open('app/src/main/java/com/gujrat/prayerwidget/PrayerWidgetProvider.kt','w').write(
'package com.gujrat.prayerwidget\n'
'import android.appwidget.AppWidgetManager\n'
'import android.appwidget.AppWidgetProvider\n'
'import android.content.Context\n'
'import android.content.Intent\n'
'import android.widget.RemoteViews\n'
'import java.util.Calendar\n'
'import kotlin.math.*\n'
'class PrayerWidgetProvider : AppWidgetProvider() {\n'
'    override fun onUpdate(context: Context, appWidgetManager: AppWidgetManager, appWidgetIds: IntArray) {\n'
'        for (id in appWidgetIds) updateWidget(context, appWidgetManager, id)\n'
'        context.startService(Intent(context, PrayerUpdateService::class.java))\n'
'    }\n'
'    override fun onDisabled(context: Context) { context.stopService(Intent(context, PrayerUpdateService::class.java)) }\n'
'    companion object {\n'
'        const val LAT = 32.5736\n'
'        const val LNG = 74.0874\n'
'        const val TZ = 5.0\n'
'        fun calcPrayerTimes(cal: Calendar): List<Triple<String,Int,String>> {\n'
'            val y = cal.get(Calendar.YEAR)\n'
'            val m = cal.get(Calendar.MONTH)+1\n'
'            val d = cal.get(Calendar.DAY_OF_MONTH)\n'
'            val jd = 367.0*y - (7*(y+(m+9)/12)/4) + (275*m/9) + d + 1721013.5\n'
'            val D = jd - 2451545.0\n'
'            val g = Math.toRadians(357.529 + 0.98560028*D)\n'
'            val L = 280.459 + 0.98564736*D\n'
'            val lam = Math.toRadians(L + 1.9148*sin(g) + 0.02*sin(2*g))\n'
'            val ep = Math.toRadians(23.439 - 0.00000036*D)\n'
'            val RA = Math.toDegrees(atan2(cos(ep)*sin(lam), cos(lam)))/15.0\n'
'            val decl = Math.toDegrees(asin(sin(ep)*sin(lam)))\n'
'            val eqT = (L - 0.0057183 - RA*15)/15.0\n'
'            val noon = 12.0 + TZ - LNG/15.0 - eqT\n'
'            fun hourAngle(angle: Double): Double {\n'
'                val cosH = (sin(Math.toRadians(angle)) - sin(Math.toRadians(LAT))*sin(Math.toRadians(decl))) / (cos(Math.toRadians(LAT))*cos(Math.toRadians(decl)))\n'
'                return Math.toDegrees(acos(cosH.coerceIn(-1.0,1.0)))/15.0\n'
'            }\n'
'            val fajr = noon - hourAngle(-18.0)\n'
'            val dhuhr = noon\n'
'            val asrAngle = Math.toDegrees(atan(1.0 + tan(Math.toRadians(abs(LAT - decl)))))\n'
'            val cosAsr = (sin(Math.toRadians(90.0-asrAngle)) - sin(Math.toRadians(LAT))*sin(Math.toRadians(decl))) / (cos(Math.toRadians(LAT))*cos(Math.toRadians(decl)))\n'
'            val asr = noon + Math.toDegrees(acos(cosAsr.coerceIn(-1.0,1.0)))/15.0\n'
'            val maghrib = noon + hourAngle(-0.833)\n'
'            val isha = noon + hourAngle(-18.0)\n'
'            fun fmt(t: Double): Pair<Int,String> {\n'
'                val tt = ((t % 24) + 24) % 24\n'
'                val h = tt.toInt(); val min = ((tt-h)*60).toInt()\n'
'                val ampm = if(h<12) "AM" else "PM"\n'
'                val h12 = if(h%12==0) 12 else h%12\n'
'                return Pair(h*60+min, "$h12:${min.toString().padStart(2,\'0\')} $ampm")\n'
'            }\n'
'            val (fm,fs)=fmt(fajr); val (dm,ds)=fmt(dhuhr); val (am,as_)=fmt(asr); val (mm,ms)=fmt(maghrib); val (im,is_)=fmt(isha)\n'
'            return listOf(Triple("Fajr",fm,fs),Triple("Dhuhr",dm,ds),Triple("Asr",am,as_),Triple("Maghrib",mm,ms),Triple("Isha",im,is_))\n'
'        }\n'
'        fun updateWidget(context: Context, appWidgetManager: AppWidgetManager, appWidgetId: Int) {\n'
'            val views = RemoteViews(context.packageName, R.layout.prayer_widget_layout)\n'
'            val cal = Calendar.getInstance()\n'
'            val prayers = calcPrayerTimes(cal)\n'
'            val now = cal.get(Calendar.HOUR_OF_DAY)*60+cal.get(Calendar.MINUTE)\n'
'            val sec = cal.get(Calendar.SECOND)\n'
'            var next = prayers[0]; var diff = Int.MAX_VALUE\n'
'            for (p in prayers) { val d=p.second-now; if(d>0&&d<diff){diff=d;next=p} }\n'
'            if(diff==Int.MAX_VALUE){next=prayers[0];diff=1440-now+prayers[0].second}\n'
'            val total=diff*60-sec\n'
'            views.setTextViewText(R.id.widget_prayer_name,next.first)\n'
'            views.setTextViewText(R.id.widget_prayer_time,next.third)\n'
'            views.setTextViewText(R.id.widget_countdown,String.format("%02d:%02d:%02d",total/3600,(total%3600)/60,total%60))\n'
'            views.setTextViewText(R.id.widget_location,"Gujrat")\n'
'            val ids=listOf(Triple(R.id.fajr_name,R.id.fajr_time,prayers[0]),Triple(R.id.dhuhr_name,R.id.dhuhr_time,prayers[1]),Triple(R.id.asr_name,R.id.asr_time,prayers[2]),Triple(R.id.maghrib_name,R.id.maghrib_time,prayers[3]),Triple(R.id.isha_name,R.id.isha_time,prayers[4]))\n'
'            for((nId,tId,p) in ids){val c=if(p.first==next.first)0xFF10B981.toInt() else 0xCCFFFFFF.toInt();views.setTextColor(nId,c);views.setTextColor(tId,if(p.first==next.first)0xFF10B981.toInt() else 0x88FFFFFF.toInt());views.setTextViewText(tId,p.third)}\n'
'            appWidgetManager.updateAppWidget(appWidgetId,views)\n'
'        }\n'
'    }\n'
'}\n')

open('app/src/main/java/com/gujrat/prayerwidget/PrayerUpdateService.kt','w').write('package com.gujrat.prayerwidget\nimport android.app.Service\nimport android.appwidget.AppWidgetManager\nimport android.content.ComponentName\nimport android.content.Intent\nimport android.os.Handler\nimport android.os.IBinder\nimport android.os.Looper\nclass PrayerUpdateService : Service() {\n    private val handler=Handler(Looper.getMainLooper())\n    private lateinit var runnable: Runnable\n    override fun onStartCommand(intent: Intent?,flags: Int,startId: Int): Int {\n        runnable=Runnable{val mgr=AppWidgetManager.getInstance(this);val ids=mgr.getAppWidgetIds(ComponentName(this,PrayerWidgetProvider::class.java));for(id in ids)PrayerWidgetProvider.updateWidget(this,mgr,id);handler.postDelayed(runnable,1000)}\n        handler.post(runnable);return START_STICKY\n    }\n    override fun onDestroy(){handler.removeCallbacks(runnable);super.onDestroy()}\n    override fun onBind(intent: Intent?): IBinder?=null\n}\n')

open('app/src/main/java/com/gujrat/prayerwidget/BootReceiver.kt','w').write('package com.gujrat.prayerwidget\nimport android.content.BroadcastReceiver\nimport android.content.Context\nimport android.content.Intent\nclass BootReceiver : BroadcastReceiver() {\n    override fun onReceive(context: Context,intent: Intent) {\n        if(intent.action==Intent.ACTION_BOOT_COMPLETED) context.startService(Intent(context,PrayerUpdateService::class.java))\n    }\n}\n')

open('gradle.properties','w').write('android.useAndroidX=true\nandroid.enableJetifier=true\n')
open('build.gradle','w').write('plugins {\n id "com.android.application" version "8.3.0" apply false\n id "org.jetbrains.kotlin.android" version "1.9.0" apply false\n}\n')
open('app/build.gradle','w').write('plugins {\n id "com.android.application"\n id "org.jetbrains.kotlin.android"\n}\nandroid {\n namespace "com.gujrat.prayerwidget"\n compileSdk 34\n defaultConfig {\n applicationId "com.gujrat.prayerwidget"\n minSdk 26\n targetSdk 34\n versionCode 1\n versionName "1.0"\n }\n compileOptions {\n sourceCompatibility JavaVersion.VERSION_17\n targetCompatibility JavaVersion.VERSION_17\n }\n kotlinOptions { jvmTarget = "17" }\n}\ndependencies {\n implementation "androidx.core:core-ktx:1.12.0"\n implementation "androidx.appcompat:appcompat:1.6.1"\n}\n')
open('settings.gradle','w').write('pluginManagement {\n repositories { google(); mavenCentral(); gradlePluginPortal() }\n}\ndependencyResolutionManagement {\n repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)\n repositories { google(); mavenCentral() }\n}\nrootProject.name = "PrayerWidget"\ninclude ":app"\n')
open('gradle/wrapper/gradle-wrapper.properties','w').write('distributionBase=GRADLE_USER_HOME\ndistributionPath=wrapper/dists\ndistributionUrl=https\\://services.gradle.org/distributions/gradle-8.4-bin.zip\nzipStoreBase=GRADLE_USER_HOME\nzipStorePath=wrapper/dists\n')

urllib.request.urlretrieve('https://raw.githubusercontent.com/gradle/gradle/v8.4.0/gradlew','gradlew')
os.chmod('gradlew',0o755)
print('All files created!')
