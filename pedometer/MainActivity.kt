package com.example.internship_pedometer

import android.Manifest.permission.ACTIVITY_RECOGNITION
import android.content.Context
import android.content.pm.PackageManager
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import com.example.internship_pedometer.ui.theme.Internship_pedometerTheme

class MainActivity : ComponentActivity(), SensorEventListener {

    private lateinit var stepCountView: TextView
    private lateinit var resetButton: Button
    private lateinit var sensorManager: SensorManager
    private var stepCountSensor: Sensor? = null


    private var currentSteps = 0;

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // View 초기화
        stepCountView = findViewById(R.id.stepCountView)
        resetButton = findViewById(R.id.resetButton)

        // 활동 퍼미션 체크
        if (ContextCompat.checkSelfPermission(this, ACTIVITY_RECOGNITION) == PackageManager.PERMISSION_DENIED) {
            ActivityCompat.requestPermissions(this, arrayOf(ACTIVITY_RECOGNITION), 0)
        }

        // 걸음 센서 연결

        sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager
        stepCountSensor = sensorManager.getDefaultSensor(Sensor.TYPE_STEP_DETECTOR)


        // 디바이스에 걸음 센서의 존재 여부 체크
        if (stepCountSensor == null){
            Toast.makeText(this, "No Step Sensor",
                Toast.LENGTH_SHORT).show()
        }

        // 리셋 기능
        resetButton.setOnClickListener {
            // 현재 걸음수 초기화
            currentSteps = 0
            stepCountView.text = currentSteps.toString()
        }
    }

    public override fun onStart(){
        super.onStart()

            // 센서 속도 설정
            // * 옵션
            // - SENSOR_DELAY_NORMAL: 20,000 초 딜레이
            // - SENSOR_DELAY_UI: 6,000 초 딜레이
            // - SENSOR_DELAY_GAME: 20,000 초 딜레이
            // - SENSOR_DELAY_FASTEST: 딜레이 없음
            //

        if(stepCountSensor != null)
            sensorManager.registerListener(this, stepCountSensor, SensorManager.SENSOR_DELAY_FASTEST)
        }

    override fun onSensorChanged(event : SensorEvent){
        if(event.sensor.getType() == Sensor.TYPE_STEP_DETECTOR){
            if(event.values[0] == 1.0f){
                currentSteps++;
                stepCountView.text = currentSteps.toString()
            }
        }
    }

    override fun onAccuracyChanged(sensor : Sensor, accuracy : Int){

    }
}
