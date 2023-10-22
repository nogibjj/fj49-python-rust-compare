extern crate sysinfo;
use std::time::Instant;
use std::process::{Command, Stdio};
use std::io::Read;
use sysinfo::{System, SystemExt};

fn main() {
    let start_time = Instant::now();

    // Execute your main script (replace 'main' with your actual binary name)
    let mut main_process = Command::new("./target/debug/main")
        .stdout(Stdio::piped())
        .spawn()
        .expect("Failed to execute main.rs");

    let _main_output = if let Some(ref mut stdout) = main_process.stdout {
        let mut output = String::new();
        stdout.read_to_string(&mut output).expect("Failed to read stdout");
        output
    } 
    else {
        String::new()
    };
    
    main_process.wait().expect("Failed to wait for main.rs to finish");


    println!("Performance of rust script file:");

    let end_time = start_time.elapsed();
    println!("Execution Time: {:.4?}", end_time);

    // Initialize a System object for system monitoring
    let sys = System::new_all();

    let memory_info = sys.get_used_memory() / (1024 * 1024); // Memory usage in MB
    println!("Memory Consumption: {:.4} MB", memory_info);

    println!(" ---------- END -----------");
}
