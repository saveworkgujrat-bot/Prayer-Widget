import os
import urllib.request

os.makedirs('app/src/main/java/com/gujrat/prayerwidget', exist_ok=True)
os.makedirs('app/src/main/res/xml', exist_ok=True)
os.makedirs('app/src/main/res/layout', exist_ok=True)
os.makedirs('app/src/main/res/values', exist_ok=True)
os.makedirs('gradle/wrapper', exist_ok=True)

open('app/src/main/AndroidManifest.xml','w').write('''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <application android:allowBackup="true" android:label="Prayer Widget" android:theme="@android:style/Theme.DeviceDefault">

        <receiver android:name=".PrayerWidgetProvider" android:exported="true">
            <intent-filter><action android:name="android.appwidget.action.APPWIDGET_UPDATE" /></intent-filter>
            <meta-data android:name="android.appwidget.provider" android:resource="@xml/prayer_widget_info" />
        </receiver>

        <receiver android:name=".PrayerWidgetMinimal" android:exported="true">
            <intent-filter><action android:name="android.appwidget.action.APPWIDGET_UPDATE" /></intent-filter>
            <meta-data android:name="android.appwidget.provider" android:resource="@xml/prayer_widget_info2" />
        </receiver>

        <receiver android:name=".PrayerWidgetFull" android:exported="true">
            <intent-filter><action android:name="android.appwidget.action.APPWIDGET_UPDATE" /></intent-filter>
            <meta-data android:name="android.appwidget.provider" android:resource="@xml/prayer_widget_info3" />
        </receiver>

        <receiver android:name=".PrayerWidgetCard" android:exported="true">
            <intent-filter><action android:name="android.appwidget.action.APPWIDGET_UPDATE" /></intent-filter>
            <meta-data android:name="android.appwidget.provider" android:resource="@xml/prayer_widget_info4" />
        </receiver>

        <service android:name=".PrayerUpdateService" android:exported="false" />
        <receiver android:name=".BootReceiver" android:exported="true">
            <intent-filter><action android:name="android.intent.action.BOOT_COMPLETED" /></intent-filter>
        </receiver>
    </application>
</manifest>
''')

# Widget info files
widgets = [('','widget_desc_classic'),('2','widget_desc_minimal'),('3','widget_desc_full'),('4','widget_desc_cards')]
for idx, desc in widgets:
    xml = '<?xml version="1.0" encoding="utf-8"?>\n'
    xml += '<appwidget-provider xmlns:android="http://schemas.android.com/apk/res/android"\n'
    xml += '    android:minWidth="250dp"\n'
    xml += '    android:minHeight="110dp"\n'
    xml += '    android:targetCellWidth="4"\n'
    xml += '    android:targetCellHeight="2"\n'
    xml += '    android:updatePeriodMillis="1800000"\n'
    xml += f'    android:initialLayout="@layout/prayer_widget_layout{idx}"\n'
    xml += f'    android:previewLayout="@layout/prayer_widget_layout{idx}"\n'
    xml += '    android:resizeMode="horizontal|vertical"\n'
    xml += '    android:widgetCategory="home_screen"\n'
    xml += f'    android:description="@string/{desc}">\n'
    xml += '</appwidget-provider>\n'
    open(f'app/src/main/res/xml/prayer_widget_info{idx}.xml','w').write(xml)


# Layout 1 — Classic (existing)
open('app/src/main/res/layout/prayer_widget_layout.xml','w').write(
'<?xml version="1.0" encoding="utf-8"?>\n'
'<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"\n'
'    android:layout_width="match_parent" android:layout_height="match_parent"\n'
'    android:orientation="horizontal" android:padding="12dp" android:background="#CC000000">\n'
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
'            android:text="TODAY SCHEDULE" android:textColor="#7AADA0" android:textSize="9sp"\n'
'            android:gravity="center" android:layout_marginBottom="5dp"/>\n'
'        <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="4dp"><TextView android:id="@+id/fajr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Fajr" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold"/><TextView android:id="@+id/fajr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="3:15 AM" android:textColor="#88FFFFFF" android:textSize="13sp"/></LinearLayout>\n'
'        <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="4dp"><TextView android:id="@+id/dhuhr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Dhuhr" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold"/><TextView android:id="@+id/dhuhr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="12:05 PM" android:textColor="#88FFFFFF" android:textSize="13sp"/></LinearLayout>\n'
'        <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="4dp"><TextView android:id="@+id/asr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Asr" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold"/><TextView android:id="@+id/asr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="5:03 PM" android:textColor="#88FFFFFF" android:textSize="13sp"/></LinearLayout>\n'
'        <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="4dp"><TextView android:id="@+id/maghrib_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Maghrib" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold"/><TextView android:id="@+id/maghrib_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="7:14 PM" android:textColor="#88FFFFFF" android:textSize="13sp"/></LinearLayout>\n'
'        <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal"><TextView android:id="@+id/isha_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Isha" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold"/><TextView android:id="@+id/isha_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="8:55 PM" android:textColor="#88FFFFFF" android:textSize="13sp"/></LinearLayout>\n'
'    </LinearLayout>\n'
'</LinearLayout>\n')

# Layout 2 — Minimal
open('app/src/main/res/layout/prayer_widget_layout2.xml','w').write('''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent" android:layout_height="match_parent"
    android:orientation="vertical" android:gravity="center"
    android:padding="16dp" android:background="#CC0D1B2A">
    <TextView android:layout_width="wrap_content" android:layout_height="wrap_content"
        android:text="NEXT PRAYER" android:textColor="#7AADA0" android:textSize="10sp" android:letterSpacing="0.2"/>
    <TextView android:id="@+id/widget_prayer_name" android:layout_width="wrap_content"
        android:layout_height="wrap_content" android:text="Asr"
        android:textColor="#FFFFFF" android:textSize="36sp" android:textStyle="bold"/>
    <TextView android:id="@+id/widget_prayer_time" android:layout_width="wrap_content"
        android:layout_height="wrap_content" android:text="5:03 PM"
        android:textColor="#10B981" android:textSize="16sp"/>
    <TextView android:id="@+id/widget_countdown" android:layout_width="wrap_content"
        android:layout_height="wrap_content" android:text="01:49:52"
        android:textColor="#FFFFFF" android:textSize="28sp" android:textStyle="bold" android:layout_marginTop="4dp"/>
    <TextView android:id="@+id/widget_location" android:layout_width="wrap_content"
        android:layout_height="wrap_content" android:text="Gujrat"
        android:textColor="#10B981" android:textSize="11sp" android:layout_marginTop="4dp"/>
    <TextView android:id="@+id/fajr_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/fajr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/dhuhr_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/dhuhr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/asr_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/asr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/maghrib_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/maghrib_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/isha_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/isha_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
</LinearLayout>
''')

# Layout 3 — Full Schedule
open('app/src/main/res/layout/prayer_widget_layout3.xml','w').write('''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent" android:layout_height="match_parent"
    android:orientation="vertical" android:padding="10dp" android:background="#CC0D1B2A">
    <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:gravity="center_vertical" android:layout_marginBottom="6dp">
        <TextView android:id="@+id/widget_prayer_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Asr" android:textColor="#10B981" android:textSize="18sp" android:textStyle="bold"/>
        <TextView android:id="@+id/widget_countdown" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="01:49:52" android:textColor="#FFFFFF" android:textSize="18sp" android:textStyle="bold"/>
    </LinearLayout>
    <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="4dp"><TextView android:id="@+id/fajr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Fajr" android:textColor="#CCFFFFFF" android:textSize="14sp" android:textStyle="bold"/><TextView android:id="@+id/fajr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="3:15 AM" android:textColor="#88FFFFFF" android:textSize="14sp"/></LinearLayout>
    <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="4dp"><TextView android:id="@+id/dhuhr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Dhuhr" android:textColor="#CCFFFFFF" android:textSize="14sp" android:textStyle="bold"/><TextView android:id="@+id/dhuhr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="12:05 PM" android:textColor="#88FFFFFF" android:textSize="14sp"/></LinearLayout>
    <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="4dp"><TextView android:id="@+id/asr_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Asr" android:textColor="#CCFFFFFF" android:textSize="14sp" android:textStyle="bold"/><TextView android:id="@+id/asr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="5:03 PM" android:textColor="#88FFFFFF" android:textSize="14sp"/></LinearLayout>
    <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal" android:layout_marginBottom="4dp"><TextView android:id="@+id/maghrib_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Maghrib" android:textColor="#CCFFFFFF" android:textSize="14sp" android:textStyle="bold"/><TextView android:id="@+id/maghrib_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="7:14 PM" android:textColor="#88FFFFFF" android:textSize="14sp"/></LinearLayout>
    <LinearLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:orientation="horizontal"><TextView android:id="@+id/isha_name" android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:text="Isha" android:textColor="#CCFFFFFF" android:textSize="14sp" android:textStyle="bold"/><TextView android:id="@+id/isha_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="8:55 PM" android:textColor="#88FFFFFF" android:textSize="14sp"/></LinearLayout>
    <TextView android:id="@+id/widget_prayer_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/widget_location" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
</LinearLayout>
''')

# Layout 4 — Cards
open('app/src/main/res/layout/prayer_widget_layout4.xml','w').write('''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent" android:layout_height="match_parent"
    android:orientation="horizontal" android:padding="6dp" android:background="#CC0D1B2A">
    <LinearLayout android:layout_width="0dp" android:layout_height="match_parent" android:layout_weight="1" android:orientation="vertical" android:gravity="center" android:background="#331A5C38" android:layout_marginEnd="3dp">
        <TextView android:id="@+id/fajr_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="Fajr" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold" android:gravity="center"/>
        <TextView android:id="@+id/fajr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="3:15 AM" android:textColor="#10B981" android:textSize="11sp" android:gravity="center"/>
    </LinearLayout>
    <LinearLayout android:layout_width="0dp" android:layout_height="match_parent" android:layout_weight="1" android:orientation="vertical" android:gravity="center" android:background="#331A5C38" android:layout_marginEnd="3dp">
        <TextView android:id="@+id/dhuhr_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="Dhuhr" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold" android:gravity="center"/>
        <TextView android:id="@+id/dhuhr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="12:05 PM" android:textColor="#10B981" android:textSize="11sp" android:gravity="center"/>
    </LinearLayout>
    <LinearLayout android:layout_width="0dp" android:layout_height="match_parent" android:layout_weight="1" android:orientation="vertical" android:gravity="center" android:background="#331A5C38" android:layout_marginEnd="3dp">
        <TextView android:id="@+id/asr_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="Asr" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold" android:gravity="center"/>
        <TextView android:id="@+id/asr_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="5:03 PM" android:textColor="#10B981" android:textSize="11sp" android:gravity="center"/>
    </LinearLayout>
    <LinearLayout android:layout_width="0dp" android:layout_height="match_parent" android:layout_weight="1" android:orientation="vertical" android:gravity="center" android:background="#331A5C38" android:layout_marginEnd="3dp">
        <TextView android:id="@+id/maghrib_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="Maghrib" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold" android:gravity="center"/>
        <TextView android:id="@+id/maghrib_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="7:14 PM" android:textColor="#10B981" android:textSize="11sp" android:gravity="center"/>
    </LinearLayout>
    <LinearLayout android:layout_width="0dp" android:layout_height="match_parent" android:layout_weight="1" android:orientation="vertical" android:gravity="center" android:background="#331A5C38">
        <TextView android:id="@+id/isha_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="Isha" android:textColor="#CCFFFFFF" android:textSize="13sp" android:textStyle="bold" android:gravity="center"/>
        <TextView android:id="@+id/isha_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="8:55 PM" android:textColor="#10B981" android:textSize="11sp" android:gravity="center"/>
    </LinearLayout>
    <TextView android:id="@+id/widget_prayer_name" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/widget_prayer_time" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/widget_countdown" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
    <TextView android:id="@+id/widget_location" android:layout_width="wrap_content" android:layout_height="wrap_content" android:visibility="gone"/>
</LinearLayout>
''')

open('app/src/main/res/values/strings.xml','w').write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <string name="app_name">Prayer Widget</string>\n    <string name="widget_desc_classic">Classic Style</string>\n    <string name="widget_desc_minimal">Minimal Style</string>\n    <string name="widget_desc_full">Full Schedule</string>\n    <string name="widget_desc_cards">Cards Style</string>\n</resources>\n')

# All 4 widget providers
kt_common = '''package com.gujrat.prayerwidget
import android.appwidget.AppWidgetManager
import android.appwidget.AppWidgetProvider
import android.content.Context
import android.content.Intent
import android.widget.RemoteViews
import java.util.Calendar
'''

update_fn = '''
    companion object {
        val PRAYERS = listOf(Triple("Fajr",3*60+15,"3:15 AM"),Triple("Dhuhr",12*60+5,"12:05 PM"),Triple("Asr",17*60+3,"5:03 PM"),Triple("Maghrib",19*60+14,"7:14 PM"),Triple("Isha",20*60+55,"8:55 PM"))
        fun updateWidget(context: Context, appWidgetManager: AppWidgetManager, appWidgetId: Int, layout: Int) {
            val views = RemoteViews(context.packageName, layout)
            val cal = Calendar.getInstance()
            val now = cal.get(Calendar.HOUR_OF_DAY)*60+cal.get(Calendar.MINUTE)
            val sec = cal.get(Calendar.SECOND)
            var next = PRAYERS[0]; var diff = Int.MAX_VALUE
            for (p in PRAYERS) { val d=p.second-now; if(d>0&&d<diff){diff=d;next=p} }
            if(diff==Int.MAX_VALUE){next=PRAYERS[0];diff=1440-now+PRAYERS[0].second}
            val total=diff*60-sec
            views.setTextViewText(R.id.widget_prayer_name,next.first)
            views.setTextViewText(R.id.widget_prayer_time,next.third)
            views.setTextViewText(R.id.widget_countdown,String.format("%02d:%02d:%02d",total/3600,(total%3600)/60,total%60))
            views.setTextViewText(R.id.widget_location,"Gujrat")
            val ids=listOf(Triple(R.id.fajr_name,R.id.fajr_time,PRAYERS[0]),Triple(R.id.dhuhr_name,R.id.dhuhr_time,PRAYERS[1]),Triple(R.id.asr_name,R.id.asr_time,PRAYERS[2]),Triple(R.id.maghrib_name,R.id.maghrib_time,PRAYERS[3]),Triple(R.id.isha_name,R.id.isha_time,PRAYERS[4]))
            for((nId,tId,p) in ids){views.setTextColor(nId,if(p.first==next.first)0xFF10B981.toInt() else 0xCCFFFFFF.toInt());views.setTextColor(tId,if(p.first==next.first)0xFF10B981.toInt() else 0x88FFFFFF.toInt());views.setTextViewText(tId,p.third)}
            appWidgetManager.updateAppWidget(appWidgetId,views)
        }
    }
'''

for cls, layout in [('PrayerWidgetProvider','R.layout.prayer_widget_layout'),('PrayerWidgetMinimal','R.layout.prayer_widget_layout2'),('PrayerWidgetFull','R.layout.prayer_widget_layout3'),('PrayerWidgetCard','R.layout.prayer_widget_layout4')]:
    open(f'app/src/main/java/com/gujrat/prayerwidget/{cls}.kt','w').write(
        kt_common +
        f'class {cls} : AppWidgetProvider() {{\n'
        f'    override fun onUpdate(context: Context, appWidgetManager: AppWidgetManager, appWidgetIds: IntArray) {{\n'
        f'        for (id in appWidgetIds) updateWidget(context, appWidgetManager, id, {layout})\n'
        f'        context.startService(Intent(context, PrayerUpdateService::class.java))\n'
        f'    }}\n'
        f'    override fun onDisabled(context: Context) {{ context.stopService(Intent(context, PrayerUpdateService::class.java)) }}\n'
        + update_fn +
        '}\n'
    )

open('app/src/main/java/com/gujrat/prayerwidget/PrayerUpdateService.kt','w').write('package com.gujrat.prayerwidget\nimport android.app.Service\nimport android.appwidget.AppWidgetManager\nimport android.content.ComponentName\nimport android.content.Intent\nimport android.os.Handler\nimport android.os.IBinder\nimport android.os.Looper\nclass PrayerUpdateService : Service() {\n    private val handler=Handler(Looper.getMainLooper())\n    private lateinit var runnable: Runnable\n    override fun onStartCommand(intent: Intent?,flags: Int,startId: Int): Int {\n        runnable=Runnable{\n            val mgr=AppWidgetManager.getInstance(this)\n            for(cls in listOf(PrayerWidgetProvider::class.java,PrayerWidgetMinimal::class.java,PrayerWidgetFull::class.java,PrayerWidgetCard::class.java)){\n                val ids=mgr.getAppWidgetIds(ComponentName(this,cls))\n            }\n            handler.postDelayed(runnable,1000)}\n        handler.post(runnable);return START_STICKY\n    }\n    override fun onDestroy(){handler.removeCallbacks(runnable);super.onDestroy()}\n    override fun onBind(intent: Intent?): IBinder?=null\n}\n')

open('app/src/main/java/com/gujrat/prayerwidget/BootReceiver.kt','w').write('package com.gujrat.prayerwidget\nimport android.content.BroadcastReceiver\nimport android.content.Context\nimport android.content.Intent\nclass BootReceiver : BroadcastReceiver() {\n    override fun onReceive(context: Context,intent: Intent) {\n        if(intent.action==Intent.ACTION_BOOT_COMPLETED) context.startService(Intent(context,PrayerUpdateService::class.java))\n    }\n}\n')

open('gradle.properties','w').write('android.useAndroidX=true\nandroid.enableJetifier=true\n')
open('build.gradle','w').write('plugins {\n id "com.android.application" version "8.3.0" apply false\n id "org.jetbrains.kotlin.android" version "1.9.0" apply false\n}\n')
open('app/build.gradle','w').write('plugins {\n id "com.android.application"\n id "org.jetbrains.kotlin.android"\n}\nandroid {\n namespace "com.gujrat.prayerwidget"\n compileSdk 34\n defaultConfig {\n applicationId "com.gujrat.prayerwidget"\n minSdk 26\n targetSdk 34\n versionCode 1\n versionName "1.0"\n }\n compileOptions {\n sourceCompatibility JavaVersion.VERSION_17\n targetCompatibility JavaVersion.VERSION_17\n }\n kotlinOptions { jvmTarget = "17" }\n}\ndependencies {\n implementation "androidx.core:core-ktx:1.12.0"\n implementation "androidx.appcompat:appcompat:1.6.1"\n}\n')
open('settings.gradle','w').write('pluginManagement {\n repositories { google(); mavenCentral(); gradlePluginPortal() }\n}\ndependencyResolutionManagement {\n repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)\n repositories { google(); mavenCentral() }\n}\nrootProject.name = "PrayerWidget"\ninclude ":app"\n')
open('gradle/wrapper/gradle-wrapper.properties','w').write('distributionBase=GRADLE_USER_HOME\ndistributionPath=wrapper/dists\ndistributionUrl=https\\://services.gradle.org/distributions/gradle-8.4-bin.zip\nzipStoreBase=GRADLE_USER_HOME\nzipStorePath=wrapper/dists\n')

urllib.request.urlretrieve('https://raw.githubusercontent.com/gradle/gradle/v8.4.0/gradlew','gradlew')
os.chmod('gradlew',0o755)
print('All files created!')
