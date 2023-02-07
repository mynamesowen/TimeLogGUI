namespace TimeLog
{
    partial class MainWindow
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.entryGroup = new System.Windows.Forms.GroupBox();
            this.entryDatePicker = new System.Windows.Forms.DateTimePicker();
            this.dateLabel = new System.Windows.Forms.Label();
            this.panel1 = new System.Windows.Forms.Panel();
            this.entryGroup.SuspendLayout();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // entryGroup
            // 
            this.entryGroup.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.entryGroup.Controls.Add(this.panel1);
            this.entryGroup.Font = new System.Drawing.Font("Georgia", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.entryGroup.Location = new System.Drawing.Point(12, 12);
            this.entryGroup.Name = "entryGroup";
            this.entryGroup.Size = new System.Drawing.Size(324, 181);
            this.entryGroup.TabIndex = 0;
            this.entryGroup.TabStop = false;
            this.entryGroup.Text = "New Entry";
            this.entryGroup.Enter += new System.EventHandler(this.groupBox1_Enter);
            // 
            // entryDatePicker
            // 
            this.entryDatePicker.Font = new System.Drawing.Font("Calibri", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.entryDatePicker.Location = new System.Drawing.Point(55, 6);
            this.entryDatePicker.Name = "entryDatePicker";
            this.entryDatePicker.Size = new System.Drawing.Size(217, 22);
            this.entryDatePicker.TabIndex = 1;
            this.entryDatePicker.ValueChanged += new System.EventHandler(this.entryDatePicker_ValueChanged);
            // 
            // dateLabel
            // 
            this.dateLabel.Font = new System.Drawing.Font("Calibri", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.dateLabel.Location = new System.Drawing.Point(8, 6);
            this.dateLabel.Name = "dateLabel";
            this.dateLabel.Size = new System.Drawing.Size(41, 22);
            this.dateLabel.TabIndex = 0;
            this.dateLabel.Text = "Date:";
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.panel1.Controls.Add(this.dateLabel);
            this.panel1.Controls.Add(this.entryDatePicker);
            this.panel1.Location = new System.Drawing.Point(0, 19);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(324, 35);
            this.panel1.TabIndex = 1;
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.entryGroup);
            this.Name = "MainWindow";
            this.Text = "Time Log";
            this.entryGroup.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox entryGroup;
        private System.Windows.Forms.Label dateLabel;
        private System.Windows.Forms.DateTimePicker entryDatePicker;
        private System.Windows.Forms.Panel panel1;
    }
}

