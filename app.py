import streamlit as st
import time

# Function to convert length units
def convert_length(value, from_unit, to_unit):
    # Conversion factors to meters
    to_meter = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1.0,
        'kilometer': 1000.0,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34
    }
    
    # Convert input value to meters
    meters = value * to_meter[from_unit]
    
    # Convert meters to the target unit
    converted_value = meters / to_meter[to_unit]
    
    return converted_value

# Function to convert weight units
def convert_weight(value, from_unit, to_unit):
    # Conversion factors to grams
    to_gram = {
        'milligram': 0.001,
        'gram': 1.0,
        'kilogram': 1000.0,
        'ton': 1000000.0,
        'ounce': 28.3495,
        'pound': 453.592
    }
    
    # Convert input value to grams
    grams = value * to_gram[from_unit]
    
    # Convert grams to the target unit
    converted_value = grams / to_gram[to_unit]
    
    return converted_value

# Function to convert temperature units
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        else:
            return value
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value

# Function to convert volume units
def convert_volume(value, from_unit, to_unit):
    # Conversion factors to liters
    to_liter = {
        'milliliter': 0.001,
        'liter': 1.0,
        'gallon': 3.78541,
        'quart': 0.946353,
        'pint': 0.473176,
        'cup': 0.24,
        'fluid_ounce': 0.0295735
    }
    
    # Convert input value to liters
    liters = value * to_liter[from_unit]
    
    # Convert liters to the target unit
    converted_value = liters / to_liter[to_unit]
    
    return converted_value

# Streamlit app
def main():
    st.set_page_config(page_title="Unit Converter", page_icon="📐", layout="centered")
    st.title("🌟 Giaic Unit Converter 🌟")
    st.markdown("Welcome to the **Giaic Unit Converter**! 🚀 Convert between different units with ease. 🎉")
    
    # Sidebar for unit type selection
    st.sidebar.header("🌟 Giaic Unit Converter 🌟")
    st.sidebar.header("⚙️ **Settings & Options** ⚙️")
    unit_type = st.sidebar.selectbox("**Select Unit Type**", ["Length 📏", "Weight ⚖️", "Temperature 🌡️", "Volume 🥤"])
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🛠️ **Tools & Features**")
    st.sidebar.markdown("- **Easy Conversion**: Convert between multiple units effortlessly. 🎯")
    st.sidebar.markdown("- **Real-Time Results**: Get instant results with animations. ⚡")
    st.sidebar.markdown("- **User-Friendly**: Simple and intuitive interface. 😊")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📌 **Tips & Tricks**")
    st.sidebar.markdown("- Use the dropdown menus to select units. 🖱️")
    st.sidebar.markdown("- Enter the value you want to convert. 🔢")
    st.sidebar.markdown("- Click **Convert** to see the magic! ✨")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🚀 **About This App**")
    st.sidebar.markdown("This app is designed to help you convert between different units quickly and easily. Whether you're a student, engineer, or just curious, this tool is for you! 🎓")
    
    if unit_type == "Length 📏":
        st.header("📏 Length Converter")
        st.markdown("Convert between **millimeters**, **centimeters**, **meters**, **kilometers**, **inches**, **feet**, **yards**, and **miles**. 🛤️")
        length_units = ['millimeter', 'centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile']
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From", length_units)
        with col2:
            to_unit = st.selectbox("To", length_units)
        value = st.number_input("Enter value", value=1.0, min_value=0.0)
        if st.button("🔄 Convert", key="length_convert"):
            with st.spinner("Converting... ⏳"):
                time.sleep(1)  # Simulate a delay for animation
                result = convert_length(value, from_unit, to_unit)
                st.balloons()  # Confetti animation
                st.success(f"🎉 **{value} {from_unit}** is equal to **{result:.4f} {to_unit}** 🎉")
    
    elif unit_type == "Weight ⚖️":
        st.header("⚖️ Weight Converter")
        st.markdown("Convert between **milligrams**, **grams**, **kilograms**, **tons**, **ounces**, and **pounds**. 🏋️")
        weight_units = ['milligram', 'gram', 'kilogram', 'ton', 'ounce', 'pound']
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From", weight_units)
        with col2:
            to_unit = st.selectbox("To", weight_units)
        value = st.number_input("Enter value", value=1.0, min_value=0.0)
        if st.button("🔄 Convert", key="weight_convert"):
            with st.spinner("Converting... ⏳"):
                time.sleep(1)  # Simulate a delay for animation
                result = convert_weight(value, from_unit, to_unit)
                st.balloons()  # Confetti animation
                st.success(f"🎉 **{value} {from_unit}** is equal to **{result:.4f} {to_unit}** 🎉")
    
    elif unit_type == "Temperature 🌡️":
        st.header("🌡️ Temperature Converter")
        st.markdown("Convert between **Celsius**, **Fahrenheit**, and **Kelvin**. 🌞")
        temperature_units = ['celsius', 'fahrenheit', 'kelvin']
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From", temperature_units)
        with col2:
            to_unit = st.selectbox("To", temperature_units)
        value = st.number_input("Enter value", value=0.0)
        if st.button("🔄 Convert", key="temp_convert"):
            with st.spinner("Converting... ⏳"):
                time.sleep(1)  # Simulate a delay for animation
                result = convert_temperature(value, from_unit, to_unit)
                st.balloons()  # Confetti animation
                st.success(f"🎉 **{value} {from_unit}** is equal to **{result:.4f} {to_unit}** 🎉")
    
    elif unit_type == "Volume 🥤":
        st.header("🥤 Volume Converter")
        st.markdown("Convert between **milliliters**, **liters**, **gallons**, **quarts**, **pints**, **cups**, and **fluid ounces**. 🥛")
        volume_units = ['milliliter', 'liter', 'gallon', 'quart', 'pint', 'cup', 'fluid_ounce']
        col1, col2 = st.columns(2)
        with col1:
            from_unit = st.selectbox("From", volume_units)
        with col2:
            to_unit = st.selectbox("To", volume_units)
        value = st.number_input("Enter value", value=1.0, min_value=0.0)
        if st.button("🔄 Convert", key="volume_convert"):
            with st.spinner("Converting... ⏳"):
                time.sleep(1)  # Simulate a delay for animation
                result = convert_volume(value, from_unit, to_unit)
                st.balloons()  # Confetti animation
                st.success(f"🎉 **{value} {from_unit}** is equal to **{result:.4f} {to_unit}** 🎉")

if __name__ == "__main__":
    main()