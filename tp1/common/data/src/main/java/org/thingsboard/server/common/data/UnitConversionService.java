package org.thingsboard.server.common.data;

public final class UnitConversionService {

    private static final float KELVIN_CELSIUS_OFFSET = 273.15f;
    private static final float FAHRENHEIT_SCALE = 9.0f / 5.0f;
    private static final float FAHRENHEIT_OFFSET = 32.0f;

    private UnitConversionService() {
        // Utility class
    }

    public static float kelvinToCelsius(float kelvin) {
        return kelvin - KELVIN_CELSIUS_OFFSET;
    }

    public static float celsiusToKelvin(float celsius) {
        return celsius + KELVIN_CELSIUS_OFFSET;
    }

    public static float celsiusToFahrenheit(float celsius) {
        return (celsius * FAHRENHEIT_SCALE) + FAHRENHEIT_OFFSET;
    }

    public static float fahrenheitToCelsius(float fahrenheit) {
        return (fahrenheit - FAHRENHEIT_OFFSET) / FAHRENHEIT_SCALE;
    }

    public static float kelvinToFahrenheit(float kelvin) {
        return celsiusToFahrenheit(kelvinToCelsius(kelvin));
    }

    public static float fahrenheitToKelvin(float fahrenheit) {
        return celsiusToKelvin(fahrenheitToCelsius(fahrenheit));
    }
}
