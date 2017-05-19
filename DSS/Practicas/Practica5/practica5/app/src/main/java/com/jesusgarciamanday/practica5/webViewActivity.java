package com.jesusgarciamanday.practica5;

import android.net.http.SslError;
import android.os.Build;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.webkit.SslErrorHandler;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

/**
 * Created by jesusgarciamanday on 5/2/17.
 */

public class webViewActivity extends AppCompatActivity {

    private WebView wbView;
    private Bundle b;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout_webview);

        wbView = (WebView) findViewById(R.id.wbGame);

        wbView.setWebViewClient(new WebViewClient(){
            @Override
            public void onReceivedSslError(WebView view, SslErrorHandler handler, SslError error){
                handler.proceed();
            }
        });

        b = getIntent().getExtras();
        if(b != null){
            if (18 < Build.VERSION.SDK_INT )
                wbView.getSettings().setCacheMode(WebSettings.LOAD_NO_CACHE);

            wbView.getSettings().setCacheMode(WebSettings.LOAD_CACHE_ELSE_NETWORK);
            wbView.getSettings().setJavaScriptEnabled(true);
            wbView.getSettings().setDomStorageEnabled(true);
            wbView.loadUrl(b.getString("url"));
        }
    }
}
