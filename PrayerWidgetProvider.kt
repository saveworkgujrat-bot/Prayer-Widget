package com.gujrat.prayerwidget

import android.appwidget.AppWidgetManager
import android.appwidget.AppWidgetProvider
import android.content.Context
import android.content.Intent
import android.widget.RemoteViews
import java.util.Calendar

class PrayerWidgetProvider : AppWidgetProvider() {

    override fun onUpdate(
        context: Context,
        appWidgetManager: AppWidgetManager,
        appWidgetIds: IntArray
    ) {
        for (id in appWidgetIds) {
            updateWidget(context, appWidgetManager, id)
        }
        // Start service for live countdown
        val serviceIntent = Intent(context, PrayerUpdateService::class.java)
        context.startService(serviceIntent)
    }

    override fun onDisabled(context: Context) {
        val serviceIntent = Intent(context, PrayerUpdateService::class.java)
        context.stopService(serviceIntent)
    }

    companion object {

        // Gujrat prayer times
        val PRAYERS = listOf(
            Triple("Fajr",    3 * 60 + 15,  "3:15 AM"),
            Triple("Dhuhr",  12 * 60 + 5,   "12:05 PM"),
            Triple("Asr",    17 * 60 + 3,   "5:03 PM"),
            Triple("Maghrib",19 * 60 + 14,  "7:14 PM"),
            Triple("Isha",   20 * 60 + 55,  "8:55 PM")
        )

        fun updateWidget(
            context: Context,
            appWidgetManager: AppWidgetManager,
            appWidgetId: Int
        ) {
            val views = RemoteViews(context.packageName, R.layout.prayer_widget_layout)
            val cal = Calendar.getInstance()
            val now = cal.get(Calendar.HOUR_OF_DAY) * 60 + cal.get(Calendar.MINUTE)
            val sec = cal.get(Calendar.SECOND)

            // Find next prayer
            var nextPrayer = PRAYERS[0]
            var minDiff = Int.MAX_VALUE
            for (p in PRAYERS) {
                val diff = p.second - now
                if (diff > 0 && diff < minDiff) {
                    minDiff = diff
                    nextPrayer = p
                }
            }
            if (minDiff == Int.MAX_VALUE) {
                nextPrayer = PRAYERS[0]
                minDiff = 1440 - now + PRAYERS[0].second
            }

            val totalSecs = minDiff * 60 - sec
            val hh = totalSecs / 3600
            val mm = (totalSecs % 3600) / 60
            val ss = totalSecs % 60

            views.setTextViewText(R.id.widget_prayer_name, nextPrayer.first)
            views.setTextViewText(R.id.widget_prayer_time, nextPrayer.third)
            views.setTextViewText(R.id.widget_countdown, String.format("%02d:%02d:%02d", hh, mm, ss))
            views.setTextViewText(R.id.widget_location, "📍 Gujrat")

            // Highlight next prayer in schedule
            val scheduleIds = listOf(
                Triple(R.id.fajr_name,    R.id.fajr_time,    PRAYERS[0]),
                Triple(R.id.dhuhr_name,   R.id.dhuhr_time,   PRAYERS[1]),
                Triple(R.id.asr_name,     R.id.asr_time,     PRAYERS[2]),
                Triple(R.id.maghrib_name, R.id.maghrib_time, PRAYERS[3]),
                Triple(R.id.isha_name,    R.id.isha_time,    PRAYERS[4])
            )

            for ((nameId, timeId, prayer) in scheduleIds) {
                if (prayer.first == nextPrayer.first) {
                    views.setTextColor(nameId, 0xFF10B981.toInt())
                    views.setTextColor(timeId, 0xFF10B981.toInt())
                } else {
                    views.setTextColor(nameId, 0xCCFFFFFF.toInt())
                    views.setTextColor(timeId, 0x88AAAAAA.toInt())
                }
                views.setTextViewText(timeId, prayer.third)
            }

            appWidgetManager.updateAppWidget(appWidgetId, views)
        }
    }
}
