package com.gujrat.prayerwidget

import android.app.Service
import android.appwidget.AppWidgetManager
import android.content.ComponentName
import android.content.Intent
import android.os.Handler
import android.os.IBinder
import android.os.Looper

class PrayerUpdateService : Service() {

    private val handler = Handler(Looper.getMainLooper())
    private lateinit var runnable: Runnable

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        runnable = Runnable {
            val manager = AppWidgetManager.getInstance(this)
            val ids = manager.getAppWidgetIds(ComponentName(this, PrayerWidgetProvider::class.java))
            for (id in ids) {
                PrayerWidgetProvider.updateWidget(this, manager, id)
            }
            handler.postDelayed(runnable, 1000) // Update every second
        }
        handler.post(runnable)
        return START_STICKY
    }

    override fun onDestroy() {
        handler.removeCallbacks(runnable)
        super.onDestroy()
    }

    override fun onBind(intent: Intent?): IBinder? = null
}
