import tkinter as tk
from tkinter import ttk, messagebox

class PontsIndexCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Pont's Index Calculator")
        self.root.geometry("800x700")
        
        # Initialize variables FIRST
        self.init_variables()
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Upper Arch Tab
        self.upper_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.upper_tab, text="Upper Arch Analysis")
        self.create_upper_arch_tab()
        
        # Lower Arch Tab
        self.lower_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.lower_tab, text="Lower Arch Analysis")
        self.create_lower_arch_tab()
        
        # Results Tab
        self.results_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.results_tab, text="Results & Inference")
        self.create_results_tab()
        
    def init_variables(self):
        # Upper arch variables
        self.central_incisor = tk.DoubleVar(value=8.5)
        self.lateral_incisor = tk.DoubleVar(value=6.5)
        self.actual_anterior_width = tk.DoubleVar(value=35.0)
        self.actual_posterior_width = tk.DoubleVar(value=45.0)
        
        # Lower arch variables
        self.upper_buccal_width = tk.DoubleVar(value=38.0)
        self.upper_lingual_width = tk.DoubleVar(value=32.0)
        self.lower_actual_molar_width = tk.DoubleVar(value=42.0)
        
        # Results
        self.sum_incisors = tk.StringVar()
        self.calc_anterior_width = tk.StringVar()
        self.calc_posterior_width = tk.StringVar()
        self.anterior_diff = tk.StringVar()
        self.posterior_diff = tk.StringVar()
        self.anterior_inference = tk.StringVar()
        self.posterior_inference = tk.StringVar()
        self.lower_conversion_factor = tk.StringVar()
        self.lower_calc_anterior = tk.StringVar()
        self.lower_calc_posterior = tk.StringVar()
        self.lower_molar_diff = tk.StringVar()
        self.lower_molar_inference = tk.StringVar()
        self.calculation_steps = tk.StringVar()

    # Rest of the methods remain exactly the same...
    def create_upper_arch_tab(self):
        frame = ttk.LabelFrame(self.upper_tab, text="Upper Arch Measurements", padding="10")
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Incisors measurements
        ttk.Label(frame, text="Mesio-distal widths (mm):").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        ttk.Label(frame, text="Central Incisor:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.central_incisor, width=10).grid(row=1, column=1, sticky=tk.W)
        
        ttk.Label(frame, text="Lateral Incisor:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.lateral_incisor, width=10).grid(row=2, column=1, sticky=tk.W)
        
        # Actual widths
        ttk.Label(frame, text="Actual Arch Widths (mm):").grid(row=3, column=0, sticky=tk.W, pady=(10,5))
        
        ttk.Label(frame, text="Anterior Width (at premolars):").grid(row=4, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.actual_anterior_width, width=10).grid(row=4, column=1, sticky=tk.W)
        
        ttk.Label(frame, text="Posterior Width (at molars):").grid(row=5, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.actual_posterior_width, width=10).grid(row=5, column=1, sticky=tk.W)
        
        # Info text
        info_text = """
        Reference Points:
        - Anterior (Premolars): Lowest point of transverse fissure of 1st premolar
        - Posterior (Molars): Intersection of transverse & buccal fissures of 1st molar
        
        For deciduous molars in mixed dentition, use posterior groove of transverse fissure.
        """
        ttk.Label(frame, text=info_text, wraplength=400, justify=tk.LEFT).grid(row=6, column=0, columnspan=2, pady=10)
        
    def create_lower_arch_tab(self):
        frame = ttk.LabelFrame(self.lower_tab, text="Lower Arch Measurements", padding="10")
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Upper arch measurements needed for lower arch calculation
        ttk.Label(frame, text="Upper Arch Measurements (mm):").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        ttk.Label(frame, text="Buccal width at 1st premolars:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.upper_buccal_width, width=10).grid(row=1, column=1, sticky=tk.W)
        
        ttk.Label(frame, text="Lingual width at 1st premolars:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.upper_lingual_width, width=10).grid(row=2, column=1, sticky=tk.W)
        
        # Lower arch actual measurement
        ttk.Label(frame, text="Lower Arch Measurement (mm):").grid(row=3, column=0, sticky=tk.W, pady=(10,5))
        
        ttk.Label(frame, text="Actual Molar Width (MB cusp to MB cusp):").grid(row=4, column=0, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.lower_actual_molar_width, width=10).grid(row=4, column=1, sticky=tk.W)
        
        # Info text
        info_text = """
        Reference Points:
        - Lower Anterior: Facial contact point between 1st & 2nd premolars
        - Lower Posterior: Tip of mesiobuccal cusp of 1st permanent molar
        
        For deciduous molars in mixed dentition, use distobuccal cusp tip.
        """
        ttk.Label(frame, text=info_text, wraplength=400, justify=tk.LEFT).grid(row=5, column=0, columnspan=2, pady=10)
        
    def create_results_tab(self):
        # Upper arch results frame
        upper_frame = ttk.LabelFrame(self.results_tab, text="Upper Arch Results", padding="10")
        upper_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(upper_frame, text="Sum of Incisors:").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(upper_frame, textvariable=self.sum_incisors).grid(row=0, column=1, sticky=tk.W)
        
        ttk.Label(upper_frame, text="Calculated Anterior Width:").grid(row=1, column=0, sticky=tk.W)
        ttk.Label(upper_frame, textvariable=self.calc_anterior_width).grid(row=1, column=1, sticky=tk.W)
        
        ttk.Label(upper_frame, text="Actual Anterior Width:").grid(row=2, column=0, sticky=tk.W)
        ttk.Label(upper_frame, textvariable=self.actual_anterior_width).grid(row=2, column=1, sticky=tk.W)
        
        ttk.Label(upper_frame, text="Difference:").grid(row=3, column=0, sticky=tk.W)
        ttk.Label(upper_frame, textvariable=self.anterior_diff).grid(row=3, column=1, sticky=tk.W)
        
        ttk.Label(upper_frame, text="Inference:").grid(row=4, column=0, sticky=tk.W)
        ttk.Label(upper_frame, textvariable=self.anterior_inference, wraplength=500).grid(row=4, column=1, sticky=tk.W)
        
        ttk.Label(upper_frame, text="Calculated Posterior Width:").grid(row=5, column=0, sticky=tk.W)
        ttk.Label(upper_frame, textvariable=self.calc_posterior_width).grid(row=5, column=1, sticky=tk.W)
        
        ttk.Label(upper_frame, text="Actual Posterior Width:").grid(row=6, column=0, sticky=tk.W)
        ttk.Label(upper_frame, textvariable=self.actual_posterior_width).grid(row=6, column=1, sticky=tk.W)
        
        ttk.Label(upper_frame, text="Difference:").grid(row=7, column=0, sticky=tk.W)
        ttk.Label(upper_frame, textvariable=self.posterior_diff).grid(row=7, column=1, sticky=tk.W)
        
        ttk.Label(upper_frame, text="Inference:").grid(row=8, column=0, sticky=tk.W)
        ttk.Label(upper_frame, textvariable=self.posterior_inference, wraplength=500).grid(row=8, column=1, sticky=tk.W)
        
        # Lower arch results frame
        lower_frame = ttk.LabelFrame(self.results_tab, text="Lower Arch Results", padding="10")
        lower_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(lower_frame, text="Conversion Factor (X):").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(lower_frame, textvariable=self.lower_conversion_factor).grid(row=0, column=1, sticky=tk.W)
        
        ttk.Label(lower_frame, text="Calculated Anterior Width:").grid(row=1, column=0, sticky=tk.W)
        ttk.Label(lower_frame, textvariable=self.lower_calc_anterior).grid(row=1, column=1, sticky=tk.W)
        
        ttk.Label(lower_frame, text="Calculated Posterior Width (Pont's W):").grid(row=2, column=0, sticky=tk.W)
        ttk.Label(lower_frame, textvariable=self.lower_calc_posterior).grid(row=2, column=1, sticky=tk.W)
        
        ttk.Label(lower_frame, text="Actual Molar Width (Patient's W):").grid(row=3, column=0, sticky=tk.W)
        ttk.Label(lower_frame, textvariable=self.lower_actual_molar_width).grid(row=3, column=1, sticky=tk.W)
        
        ttk.Label(lower_frame, text="Difference:").grid(row=4, column=0, sticky=tk.W)
        ttk.Label(lower_frame, textvariable=self.lower_molar_diff).grid(row=4, column=1, sticky=tk.W)
        
        ttk.Label(lower_frame, text="Inference:").grid(row=5, column=0, sticky=tk.W)
        ttk.Label(lower_frame, textvariable=self.lower_molar_inference, wraplength=500).grid(row=5, column=1, sticky=tk.W)
        
        # Calculation steps
        steps_frame = ttk.LabelFrame(self.results_tab, text="Calculation Steps", padding="10")
        steps_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        steps_text = tk.Text(steps_frame, wrap=tk.WORD, height=10, padx=5, pady=5)
        steps_scroll = ttk.Scrollbar(steps_frame, orient=tk.VERTICAL, command=steps_text.yview)
        steps_text.configure(yscrollcommand=steps_scroll.set)
        
        steps_text.grid(row=0, column=0, sticky=tk.NSEW)
        steps_scroll.grid(row=0, column=1, sticky=tk.NS)
        
        steps_frame.grid_rowconfigure(0, weight=1)
        steps_frame.grid_columnconfigure(0, weight=1)
        
        self.steps_text = steps_text
        
        # Calculate button
        btn_frame = ttk.Frame(self.results_tab)
        btn_frame.pack(fill=tk.X, padx=5, pady=10)
        
        ttk.Button(btn_frame, text="Calculate Pont's Index", command=self.calculate).pack(pady=5)
        
    def calculate(self):
        try:
            # Clear previous steps
            self.steps_text.delete(1.0, tk.END)
            
            # Calculate upper arch values
            self.steps_text.insert(tk.END, "=== UPPER ARCH CALCULATIONS ===\n\n")
            
            # Sum of incisors
            sum_incisors = self.central_incisor.get() * 2 + self.lateral_incisor.get() * 2
            self.sum_incisors.set(f"{sum_incisors:.2f} mm")
            self.steps_text.insert(tk.END, f"1. Sum of maxillary incisors = (Central × 2) + (Lateral × 2)\n")
            self.steps_text.insert(tk.END, f"   = ({self.central_incisor.get()} × 2) + ({self.lateral_incisor.get()} × 2) = {sum_incisors:.2f} mm\n\n")
            
            # Calculate ideal widths
            ideal_anterior = sum_incisors / 0.8
            ideal_posterior = sum_incisors / 0.64
            
            self.calc_anterior_width.set(f"{ideal_anterior:.2f} mm")
            self.calc_posterior_width.set(f"{ideal_posterior:.2f} mm")
            
            self.steps_text.insert(tk.END, "2. Calculate ideal arch widths:\n")
            self.steps_text.insert(tk.END, f"   Ideal Anterior Width = Sum of incisors / 0.8 = {sum_incisors:.2f} / 0.8 = {ideal_anterior:.2f} mm\n")
            self.steps_text.insert(tk.END, f"   Ideal Posterior Width = Sum of incisors / 0.64 = {sum_incisors:.2f} / 0.64 = {ideal_posterior:.2f} mm\n\n")
            
            # Calculate differences
            actual_anterior = self.actual_anterior_width.get()
            actual_posterior = self.actual_posterior_width.get()
            
            anterior_diff = actual_anterior - ideal_anterior
            posterior_diff = actual_posterior - ideal_posterior
            
            self.anterior_diff.set(f"{anterior_diff:.2f} mm")
            self.posterior_diff.set(f"{posterior_diff:.2f} mm")
            
            self.steps_text.insert(tk.END, "3. Compare actual vs ideal:\n")
            self.steps_text.insert(tk.END, f"   Anterior Difference = Actual {actual_anterior:.2f} - Ideal {ideal_anterior:.2f} = {anterior_diff:.2f} mm\n")
            self.steps_text.insert(tk.END, f"   Posterior Difference = Actual {actual_posterior:.2f} - Ideal {ideal_posterior:.2f} = {posterior_diff:.2f} mm\n\n")
            
            # Determine inferences
            if anterior_diff < 0:
                self.anterior_inference.set("Arch is NARROWER than ideal. There is scope for expansion.")
            else:
                self.anterior_inference.set("Arch is WIDER than ideal. No scope for expansion.")
                
            if posterior_diff < 0:
                self.posterior_inference.set("Arch is NARROWER than ideal. There is scope for expansion.")
            else:
                self.posterior_inference.set("Arch is WIDER than ideal. No scope for expansion.")
            
            # Calculate lower arch values
            self.steps_text.insert(tk.END, "\n=== LOWER ARCH CALCULATIONS ===\n\n")
            
            # Conversion factor
            upper_buccal = self.upper_buccal_width.get()
            upper_lingual = self.upper_lingual_width.get()
            conversion_factor = upper_buccal - upper_lingual
            
            self.lower_conversion_factor.set(f"{conversion_factor:.2f} mm")
            self.steps_text.insert(tk.END, f"1. Conversion Factor (X) = Upper Buccal Width - Upper Lingual Width\n")
            self.steps_text.insert(tk.END, f"   = {upper_buccal:.2f} - {upper_lingual:.2f} = {conversion_factor:.2f} mm\n\n")
            
            # Lower anterior width
            lower_anterior = ideal_anterior - conversion_factor
            self.lower_calc_anterior.set(f"{lower_anterior:.2f} mm")
            self.steps_text.insert(tk.END, f"2. Ideal Lower Anterior Width = Upper Ideal Anterior - X\n")
            self.steps_text.insert(tk.END, f"   = {ideal_anterior:.2f} - {conversion_factor:.2f} = {lower_anterior:.2f} mm\n\n")
            
            # Lower posterior width (with 1mm reduction)
            lower_posterior = ideal_posterior - 1
            self.lower_calc_posterior.set(f"{lower_posterior:.2f} mm (Ideal - 1mm to prevent crossbite)")
            self.steps_text.insert(tk.END, f"3. Ideal Lower Posterior Width = Upper Ideal Posterior - 1mm\n")
            self.steps_text.insert(tk.END, f"   = {ideal_posterior:.2f} - 1 = {lower_posterior:.2f} mm (adjusted to prevent crossbite)\n\n")
            
            # Lower molar difference
            actual_lower_molar = self.lower_actual_molar_width.get()
            lower_molar_diff = lower_posterior - actual_lower_molar
            
            self.lower_molar_diff.set(f"{lower_molar_diff:.2f} mm")
            self.steps_text.insert(tk.END, f"4. Compare actual vs ideal lower molar width:\n")
            self.steps_text.insert(tk.END, f"   Difference = Ideal {lower_posterior:.2f} - Actual {actual_lower_molar:.2f} = {lower_molar_diff:.2f} mm\n\n")
            
            # Lower inference
            if lower_molar_diff > 0:
                self.lower_molar_inference.set("Lower arch is NARROWER than ideal. There is scope for expansion.")
            else:
                self.lower_molar_inference.set("Lower arch is WIDER than ideal. No scope for expansion.")
            
            # Add notes about limitations
            self.steps_text.insert(tk.END, "\n=== IMPORTANT NOTES ===\n")
            self.steps_text.insert(tk.END, "- Pont's Index was developed for French population and may not apply universally\n")
            self.steps_text.insert(tk.END, "- Doesn't consider basal bone width, so expansion may not always be advisable\n")
            self.steps_text.insert(tk.END, "- Values are often intentionally high to compensate for possible relapse\n")
            self.steps_text.insert(tk.END, "- Clinical judgment should always supersede numerical analysis\n")
            
        except Exception as e:
            messagebox.showerror("Calculation Error", f"An error occurred during calculation:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PontsIndexCalculator(root)
    root.mainloop()