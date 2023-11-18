function ColorTextureToggle()
{
    return(
        <span className="ColorTextureToggle">
            <span className="SubColorTextureToggle">
                <p className="ColorTitle">Color</p>
                <input type="checkbox"
                id="switch"
                class="checkbox" />
                    
                <label for="switch"
                    class="toggle">
                    <p>
                        
                    </p>
                </label>
                <p className="TextureTitle">Texture</p>
                
            </span>
        </span>
    );
}

export default ColorTextureToggle;