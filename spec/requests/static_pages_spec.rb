require 'spec_helper'

describe "Static pages" do

  describe "Home page" do

    it "should have the content 'Quote'" do
      visit '/static_pages/home'
      page.should have_content('Quote')
    end
    
    it "should have the title 'Home'" do
      visit '/static_pages/home'
      page.should have_selector('title',
                    text: "Adam's Quotes | Home")
    end
    
    it "should not have a custom page title" do
      visit '/static_pages/home'
      page.should_not have_selector('title', text: '| Home')
    end
  end
  
  describe "Help page" do
    
    it "should have the content 'Help'" do
      visit '/static_pages/help'
      page.should have_content('Help')
    end
    
    it "should have the title 'Help'" do
      visit '/static_pages/help'
      page.should have_selector('title',
                    text: "Adam's Quotes | Help")
    end
  end
  
  describe "About page" do
    
    it "should have the content 'About this site'" do
      visit '/static_pages/about'
      page.should have_content('About this site')
    end
    
    it "should have the title 'About'" do
      visit '/static_pages/about'
      page.should have_selector('title',
                    text: "Adam's Quotes | About")
    end
  end
end