package com.edusense.mobile

import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class CheckinActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_checkin)

        val btnSave = findViewById<Button>(R.id.btnSave)

        btnSave.setOnClickListener {
            Toast.makeText(
                this,
                "Check-in registrado correctamente",
                Toast.LENGTH_SHORT
            ).show()

            finish()
        }
    }
}