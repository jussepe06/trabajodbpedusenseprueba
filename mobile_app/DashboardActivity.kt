package com.edusense.mobile

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity

class DashboardActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dashboard)

        val btnCheckin = findViewById<Button>(R.id.btnCheckin)

        btnCheckin.setOnClickListener {
            val intent = Intent(this, CheckinActivity::class.java)
            startActivity(intent)
        }
    }
}