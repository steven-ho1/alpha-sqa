/**
 * Copyright © 2016-2025 The Thingsboard Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.thingsboard.server.common.data;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.within;

class UnitConversionServiceTest {

    private static final float EPSILON = 0.0001f;

    @Test
    void celsiusToKelvin_zeroCelsius_returns273Point15Kelvin() {
        assertThat(UnitConversionService.celsiusToKelvin(0.0f))
                .isCloseTo(273.15f, within(EPSILON));
    }

    @Test
    void kelvinToCelsius_273Point15Kelvin_returnsZeroCelsius() {
        assertThat(UnitConversionService.kelvinToCelsius(273.15f))
                .isCloseTo(0.0f, within(EPSILON));
    }

    @Test
    void celsiusToFahrenheit_zeroCelsius_returns32Fahrenheit() {
        assertThat(UnitConversionService.celsiusToFahrenheit(0.0f))
                .isCloseTo(32.0f, within(EPSILON));
    }

    @Test
    void fahrenheitToCelsius_32Fahrenheit_returnsZeroCelsius() {
        assertThat(UnitConversionService.fahrenheitToCelsius(32.0f))
                .isCloseTo(0.0f, within(EPSILON));
    }

    @Test
    void celsiusToFahrenheit_100Celsius_returns212Fahrenheit() {
        assertThat(UnitConversionService.celsiusToFahrenheit(100.0f))
                .isCloseTo(212.0f, within(EPSILON));
    }

    @Test
    void kelvinToFahrenheit_zeroKelvin_returnsMinus459Point67Fahrenheit() {
        assertThat(UnitConversionService.kelvinToFahrenheit(0.0f))
                .isCloseTo(-459.67f, within(EPSILON));
    }

    @Test
    void fahrenheitToKelvin_minus459Point67Fahrenheit_returnsZeroKelvin() {
        assertThat(UnitConversionService.fahrenheitToKelvin(-459.67f))
                .isCloseTo(0.0f, within(EPSILON));
    }

    @Test
    void kelvinToFahrenheit_273Point15Kelvin_returns32Fahrenheit() {
        assertThat(UnitConversionService.kelvinToFahrenheit(273.15f))
                .isCloseTo(32.0f, within(EPSILON));
    }

    @Test
    void celsiusToFahrenheitAndBack_returnsOriginalValue() {
        float original = 37.5f;
        float fahrenheit = UnitConversionService.celsiusToFahrenheit(original);
        float result = UnitConversionService.fahrenheitToCelsius(fahrenheit);
        assertThat(result).isCloseTo(original, within(EPSILON));
    }

    @Test
    void celsiusToKelvinAndBack_returnsOriginalValue() {
        float original = -40.0f;
        float kelvin = UnitConversionService.celsiusToKelvin(original);
        float result = UnitConversionService.kelvinToCelsius(kelvin);
        assertThat(result).isCloseTo(original, within(EPSILON));
    }
}
